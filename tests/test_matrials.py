from raytracerchallenge_python.material import Material
from raytracerchallenge_python.tuple import Color


def test_the_default_material():
    # Given
    m = Material()
    # Then
    assert m.color == Color(1, 1, 1)
    assert m.ambient == 0.1
    assert m.diffuse == 0.9
    assert m.specular == 0.9
    assert m.shininess == 200.0
