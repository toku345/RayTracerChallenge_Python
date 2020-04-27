from raytracerchallenge_python.world import World


def test_createing_a_world():
    # Given
    w = World()
    # Then
    assert len(w.object) == 0
    assert w.light is None
