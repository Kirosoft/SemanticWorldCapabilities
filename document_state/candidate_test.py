"""Candidate behavior only; fixture selection does not grant execution authority."""
from dataclasses import replace
from pathlib import Path
import json

from hg.relationships import SemanticNode
from candidate import propose
from semanticworld.interpretation.projection_value import lower
from semanticworld.store import InstalledView, ReadBasis
from swos.authority.application import extend
from test_type_document_state import fixture, refuses
from test_type_context_restoration import selected_read


def context():
    old, projection = fixture()
    definition = json.loads(Path(__file__).with_name('definition.json').read_text())
    order = next(item for item in old.authority.declarations if item.id == 'OdooV2Order')
    description = order.canonical()
    description['relationship_bindings'] = [
        {**binding.canonical(), 'handle': binding.id} for binding in order.relationship_bindings]
    authority = extend(old.base, [description, *definition])
    read = selected_read(old.base, authority)._replace(world=old.world, eligible_refs=old.eligible_refs)
    return read, lower(read, {'definition': [order.path, 'node/state']})


def test_candidate_returns_unique_recruited_state_without_mutation():
    read, projection = context()
    before = read.world.world
    assert propose(projection, read=read, demand={}) == 'sale'
    assert read.world.world is before and before.edges[0].target_ref == 'draft'


def test_candidate_refuses_multiple_alternative_states():
    read, projection = context()
    world = replace(read.world.world, nodes=read.world.world.nodes + (SemanticNode('cancel', 'node/state'),),
        revision='world-2')
    changed = read._replace(world=InstalledView(world, ReadBasis(read.base.revision, world.revision), (), world.revision),
        eligible_refs=read.eligible_refs | {'cancel'})
    value = lower(changed, projection.request)
    refuses(lambda: propose(value, read=changed, demand={}))


def test_candidate_refuses_when_no_scoped_alternative_exists():
    read, projection = context()
    changed = read._replace(eligible_refs=read.eligible_refs - {'sale'})
    value = lower(changed, projection.request)
    refuses(lambda: propose(value, read=changed, demand={}))
