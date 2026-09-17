"""Generate proposed application descriptions using existing HG port definitions."""
import json
from pathlib import Path

from hg.authority import load_verified_authority
from hg.model import Declaration
from hg.validation import validate_authority
from hg.yaml import loads


def descriptions(authority, hg_root):
    interpretation = next(d for d in authority.declarations if d.id == "InterpretSemanticContext")
    original = loads((Path(hg_root) / "declarations/node/capability/executablecapability/interpretsemanticcontext/InterpretSemanticContext.yaml").read_text())
    request = original["input_ports"][0]
    outputs = original["output_ports"]
    subject = {"name": "subject", "role": "source", "cardinality": {"min": 1, "max": 1},
               "value": {"kind": "reference", "target": {"kind": "instance", "type": "node/party/company"}}}
    read = {"id": "ReadCompanyContext", "axis": "node", "refines": "ExecutableCapability", "domain": "app", "authoritative": False,
            "path": "node/capability/executablecapability/readcompanycontext", "groups": ["commercial"],
            "description": "Derives an interpretation request from the HG type of an existing Company instance.",
            "guarantees": ["Reads only the Company bound to its subject reference and proposes interpretation context without mutation."],
            "input_ports": [subject], "output_ports": [request], "effects": {"ports": [], "external_io": False},
            "policies": [], "failures": []}
    read_declaration = Declaration.from_dict(read)
    process = {"id": "InspectCompanyMeaning", "axis": "node", "refines": "ExecutableProcess", "domain": "app", "authoritative": False,
        "path": "node/process/executableprocess/inspectcompanymeaning", "groups": ["commercial"],
        "description": "Reusable application Strategy deriving proposal-only meaning from an existing Company instance.",
        "guarantees": ["Preserves the World subject provenance and does not materialise interpretation results."],
        "process": {"input_ports": [subject], "output_ports": outputs, "effects": {"ports": [], "external_io": False},
            "steps": [
                {"name": "read_context", "capability": read["path"],
                 "interface_digest": read_declaration.capability_contract.interface_digest,
                 "input_bindings": [{"port": "subject", "source": {"kind": "process_input", "port": "subject"}}]},
                {"name": "interpret", "capability": interpretation.path,
                 "interface_digest": interpretation.capability_contract.interface_digest,
                 "input_bindings": [{"port": "request", "source": {"kind": "step_output", "step": "read_context", "port": "request"}}]}],
            "output_bindings": [{"port": "interpretation", "source": {"kind": "step_output", "step": "interpret", "port": "interpretation"}}]}}
    validate_authority(authority.manifest, authority.declarations + (read_declaration, Declaration.from_dict(process)), authority.primitives)
    return [read, process]


def main():
    root = Path(__file__).resolve().parent
    result = descriptions(load_verified_authority(root.parent / "HG"), root.parent / "HG")
    destination = root / "applications/company_meaning.json"
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(destination)


if __name__ == "__main__":
    main()


