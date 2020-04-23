from raytracerchallenge_python.tuple import Color
from math import pow


class Material:
    def __init__(self):
        self.color = Color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0

    def __eq__(self, other):
        return all([self.color == other.color,
                    self.ambient == other.ambient,
                    self.diffuse == other.diffuse,
                    self.specular == other.specular,
                    self.shininess == other.shininess])

    def lighting(self, light, point, eyev, normalv):
        effective_color = self.color * light.intensity
        lightv = (light.position - point).normalize()
        ambient = effective_color * self.ambient
        light_dot_normal = lightv.dot(normalv)

        black = Color(0, 0, 0)
        if light_dot_normal < 0:
            diffuse = black
            specular = black
        else:
            diffuse = effective_color * self.diffuse * light_dot_normal

            reflectv = (-lightv).reflect(normalv)
            reflect_dot_eye = reflectv.dot(eyev)
            if reflect_dot_eye <= 0:
                specular = black
            else:
                factor = pow(reflect_dot_eye, self.shininess)
                specular = light.intensity * self.specular * factor

        return ambient + diffuse + specular
