"""Typed placement result; the protected interpreter validates World context."""


def propose(object, previous, next_holder, previous_binding, next_binding):
    return {'object': object['ref'], 'previous': previous['ref'],
        'next_holder': next_holder['ref'], 'previous_binding': previous_binding,
        'next_binding': next_binding}
