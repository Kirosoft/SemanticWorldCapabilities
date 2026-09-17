"""Return typed scene subjects and supplied evidence without committing facts."""


def propose(object, source, destination, actor, room, source_evidence):
    return {'object': dict(object), 'source': dict(source), 'destination': dict(destination),
        'actor': dict(actor), 'room': dict(room), 'source_evidence': source_evidence}
