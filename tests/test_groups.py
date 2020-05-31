from raytracerchallenge_python.group import Group
from raytracerchallenge_python.matrix import identity_matrix


def test_creating_a_new_group():
    # Given
    g = Group()
    # Then
    assert g.transform == identity_matrix()
    assert len(g) == 0
