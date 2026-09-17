"""CollectForward is an ordinary SWOS-admitted Capability, not intrinsic dispatch."""
from semanticworld.interpretation.projection_collection import collect


def collect_forward(projection, *, read, demand):
    return collect(read, projection)
