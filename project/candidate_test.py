"""The admission package's bounded verification is separate from execution."""
from candidate import project


def test_project_candidate_is_callable():
    assert callable(project)
