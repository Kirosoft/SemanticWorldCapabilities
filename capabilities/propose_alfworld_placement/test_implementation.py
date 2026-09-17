from implementation import propose


def test_preserves_placement_subject_and_both_bindings():
    result = propose({'ref': 'apple'}, {'ref': 'counter'}, {'ref': 'actor'}, 'contents', 'inventory')
    assert result == {'object': 'apple', 'previous': 'counter', 'next_holder': 'actor',
        'previous_binding': 'contents', 'next_binding': 'inventory'}
