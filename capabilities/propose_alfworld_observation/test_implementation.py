from implementation import propose


def test_preserves_subjects_without_effect_application():
    arguments = {name: {'identity': name, 'type': meaning} for name, meaning in (
        ('object', 'node/resource/alfworldobject'), ('source', 'node/resource/alfworldreceptacle'),
        ('destination', 'node/resource/alfworldreceptacle'), ('actor', 'node/party/alfworldactor'),
        ('room', 'node/location/alfworldroom'))}
    arguments['source_evidence'] = 'Explicit synthetic fixture observations'
    assert propose(**arguments) == arguments
