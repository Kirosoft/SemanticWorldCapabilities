"""Run candidate test artifacts in isolated processes against one explicit HG root."""
import argparse
import os
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hg-root", type=Path, required=True)
    parser.add_argument("--unit", action="store_true", help="Only standalone tests; excludes integration obligations")
    options = parser.parse_args()
    root = Path(__file__).resolve().parent
    workspace = root.parent
    hg_root = options.hg_root.resolve(strict=True)
    if not (hg_root / "hg/__init__.py").is_file() or not (hg_root / "declarations").is_dir():
        parser.error("HG root must contain the source package and its declarations")
    paths = (hg_root, workspace / "SemanticStore", workspace / "SemanticWorldOS",
             workspace / "SemanticWorldComputer", workspace, workspace / "tests",
             workspace / "semanticworld/interpretation/tests")
    env = {**os.environ, "PYTHONPATH": os.pathsep.join(map(str, paths)), "PYTHONDONTWRITEBYTECODE": "1"}
    code = """import runpy, sys, unittest
namespace = runpy.run_path(sys.argv[1], run_name='candidate_tests')
suite = unittest.TestSuite(unittest.FunctionTestCase(value) for name, value in sorted(namespace.items())
    if name.startswith('test_') and callable(value) and getattr(value, '__module__', None) == 'candidate_tests')
result = unittest.TextTestRunner(verbosity=1).run(suite)
raise SystemExit(0 if result.testsRun and result.wasSuccessful() else 1)
"""
    pattern = "*/test_implementation.py" if options.unit else "*/test_*.py"
    tests = sorted((root / "capabilities").glob(pattern))
    failed = 0
    for test in tests:
        print(f"{test.parent.name}/{test.name}", flush=True)
        try:
            result = subprocess.run([sys.executable, "-c", code, test.name], cwd=test.parent,
                env=env, capture_output=True, text=True, timeout=45)
            print(result.stdout + result.stderr, flush=True)
            failed += result.returncode != 0
        except subprocess.TimeoutExpired:
            print("FAILED: test artifact exceeded 45 seconds", flush=True)
            failed += 1
    print(f"Test artifacts: {len(tests) - failed} passed, {failed} failed", flush=True)
    if options.unit:
        print("Unit-only run excludes integration coverage and cannot establish admission or runtime parity.")
    raise SystemExit(bool(failed) or not tests)


if __name__ == "__main__":
    main()
