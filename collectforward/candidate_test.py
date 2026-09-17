"""Bound test artifacts; operational admission and invocation are separate evidence."""
from dataclasses import replace
from pathlib import Path
import unittest

from hg.computation import SemanticEdge
from hg.relationships import SemanticNode
from hostio import decode_json
from semanticworld.interpretation.projection_transport import dump, restore
from semanticworld.interpretation.projection_value import lower, validate
from test_type_context_matching import capability, context_read, requirement, found
from test_type_genus_traversal import A, ABOUT, CLASSIFIED, demand
from candidate import collect_forward


def read_for_collection():
    definitions = decode_json((Path(__file__).parent / 'definition.json').read_bytes())
    from hg.model import Declaration
    return context_read((Declaration.from_dict(definitions[0]),
        capability('TestCollectionClassChoice', [requirement('node/class')])))


def matches(value):
    return {item['definition']: item for item in value.content['response']['evidence']['matches']}


def test_one_step_collection_retains_origin_and_does_not_follow_target_edges():
    read = read_for_collection()
    value = lower(read, demand())
    result = collect_forward(value, read=read, demand=demand())
    assert {node['ref'] for node in result.content['instances']['nodes']} == {'a', 'c1', 'doc'}
    assert 'c2' not in {node['ref'] for node in result.content['instances']['nodes']}
    assert 'node/capability/collectforward' in matches(result)
    assert 'node/capability/testcollectionclasschoice' in matches(result)
    assert validate(read, result) == result and restore(read, dump(result)) == result


def test_genus_restriction_and_empty_context_are_preserved():
    read = read_for_collection()
    restricted = collect_forward(lower(read, demand(genus=CLASSIFIED)), read=read, demand={})
    assert {node['ref'] for node in restricted.content['instances']['nodes']} == {'a', 'c1'}
    empty = collect_forward(lower(read, demand('c2')), read=read, demand={})
    assert {node['ref'] for node in empty.content['instances']['nodes']} == {'c2'}
    assert not empty.content['instances']['relationships']


def test_multiple_instance_origins_remain_one_projection():
    read = read_for_collection()
    world = read.world.world
    world = replace(world, nodes=world.nodes + (SemanticNode('a2', A),),
        edges=world.edges + (SemanticEdge('a2', A, CLASSIFIED, 'c2', 'node/class'),))
    read = read._replace(world=read.world._replace(world=world), eligible_refs=read.eligible_refs | {'a2'})
    request = {'definition': [A]}
    result = collect_forward(lower(read, request), read=read, demand=request)
    assert {node['ref'] for node in result.content['instances']['nodes']} == {'a', 'a2', 'c1', 'c2', 'doc'}
    assert result.content['response']['evidence']['source_read']['evidence']['origin_refs'] == ('a', 'a2')


def test_collection_does_not_write_or_invoke_returned_capabilities():
    read = read_for_collection()
    world = read.world
    selection = read.authority_selection
    result = collect_forward(lower(read, demand()), read=read, demand={})
    assert matches(result)
    assert read.world is world and read.authority_selection is selection
    # Only CollectForward has a candidate body here. The other returned Capability
    # has no implementation source in this fixture and cannot have been invoked.


def load_tests(loader, tests, pattern):
    return unittest.TestSuite(unittest.FunctionTestCase(value)
        for name, value in sorted(globals().items()) if name.startswith('test_') and callable(value))
