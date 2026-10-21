"""Pure post-Projection restriction over retained traversal evidence."""

from hg.mutation import SemanticWorld
from semanticworld.reference import plain
from semanticworld.store import freeze
from semanticworld.interpretation.projection_value import ProjectionValue
from semanticworld.interpretation.projection_collection import _hg_closure


def restrict_relationships(
    projection: "node/projection",
    criterion: "property/reference/referstocriterion#criterion",
    *, read, demand,
):
    criterion_value = criterion["value"]
    if criterion_value != "REFERS_TO":
        raise ValueError("unsupported relationship-definition criterion")
    evidence = plain(projection.content["response"]["evidence"])
    source_nodes = {node.ref: node.node_type for node in read.world.world.nodes}
    relationship_types = {}
    for traversal in evidence.get("traversals", ()):
        source_type = source_nodes.get(traversal["source_ref"])
        if source_type is None:
            source_type = next(node.node_type for node in projection.world.nodes
                               if node.ref == traversal["source_ref"])
        declaration = next(item for item in read.authority.declarations if item.path == source_type)
        relationship_types[traversal["binding_id"]] = {
            binding.id: binding.relationship_type for binding in declaration.relationship_bindings
        }[traversal["binding_id"]]
    selected = tuple(
        item for item in evidence.get("traversals", ())
        if relationship_types.get(item["binding_id"], "").rsplit("/", 1)[-1].upper()
        == criterion_value
    )
    selected_refs = {ref for item in selected
                     for ref in (item["source_ref"], item["target_ref"])}
    world = projection.world
    restricted_world = SemanticWorld(
        nodes=tuple(node for node in world.nodes if node.ref in selected_refs),
        properties=tuple(prop for prop in world.properties if prop.subject_ref in selected_refs),
        edges=tuple(edge for edge in world.edges
                    if edge.source_ref in selected_refs and edge.target_ref in selected_refs),
        revision=world.revision,
    )
    restricted_world = _hg_closure(read, projection, restricted_world)
    content = plain(projection.content)
    content["response"]["evidence"]["traversals"] = list(selected)
    content["response"]["evidence"]["scope_digest"] = content["response"]["evidence"].get("scope_digest")
    content["complete"] = projection.content["complete"]
    return ProjectionValue(projection.request, projection.result_bound, projection.work_bound,
                           projection.basis, freeze(content), projection.collection,
                           world=restricted_world)
