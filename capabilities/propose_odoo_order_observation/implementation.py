"""Pure typed subjects; HG and the protected host govern materialisation."""


def propose(order, current_state, next_state):
    return {'order': dict(order), 'current_state': dict(current_state),
            'next_state': dict(next_state)}
