"""Experiment-local Project realiser; no commit and no new semantic resolver."""
from semanticworld.interpretation.projection_collection import collect


def project(projection, *, read, demand):
    return collect(read, projection)
