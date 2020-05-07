from raytracerchallenge_python.tuple import Color
from math import pow


class Material:
    def __init__(self):
        self.color = Color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0
        self.pattern = None

    def __eq__(self, other):
        return all([self.color == other.color,
                    self.ambient == other.ambient,
                    self.diffuse == other.diffuse,
                    self.specular == other.specular,
                    self.shininess == other.shininess,
                    self.pattern == other.pattern])

    def lighting(self, object, light, point, eyev, normalv, in_shadow=False):
        if self.pattern:
            color = self.pattern.stripe_at_object(object, point)
        else:
            color = self.color

        effective_color = color * light.intensity
        ambient = effective_color * self.ambient
        if in_shadow:
            return ambient

        lightv = (light.position - point).normalize()
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
