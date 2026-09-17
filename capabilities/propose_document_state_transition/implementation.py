"""Return the typed replacement State; invocation has no World write authority."""


def propose(subject, binding, current_state, next_state):
    return {'next_state': next_state['ref']}
