import math
import random

class Particle(object):
    """A single particle with unit mass"""

    def __init__(self, mass, x, y, z, vx, vy, vz):
        self._mass = mass
        self._x = x
        self._y = y
        self._z = z
        self._vx = vx
        self._vy = vy
        self._vz = vz

    @property
    def mass(self):
        return self._mass

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    @property
    def vx(self):
        return self._vx

    @vx.setter
    def vx(self, value):
        self._vx = value

    @property
    def vy(self):
        return self._vy

    @vy.setter
    def vy(self, value):
        self._vy = value

    @property
    def vz(self):
        return self._vz

    @vz.setter
    def vz(self, value):
        self._vz = value

    def __str__(self):
        return '%f: %f,%f,%f,%f,%f,%f' % (self._mass, self._x, self._y, self._z, self._vx, self._vy, self._vz)

    def pos(self):
        return Vector(self._x, self._y, self._z)

    def velocity(self):
        return Vector(self._vx, self._vy, self._vz)

    def kinetic_energy(self):
        return 0.5 * self.velocity().mag()**2

    @classmethod
    def from_vectors(cls, mass, pos, vel):
        return cls(mass, pos._x, pos._y, pos._z, vel._x, vel._y, vel._z)

    @staticmethod
    def calculate_force(particle, actor):
        """Calculate the force between on particle due to actor"""
        R = actor.pos() - particle.pos()
        factor = particle.mass * actor.mass * 1.0 / R.mag() ** 3
        return R.mult(factor)

class Vector(object):

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def mag(self):
        return math.sqrt(self._x**2 + self._y**2 + self._z**2)

    def __add__(self, other):
        print other
        x = self._x + other._x
        y = self._y + other._y
        z = self._z + other._z
        return Vector(x,y,z)

    def __sub__(self, other):
        x = self._x - other._x
        y = self._y - other._y
        z = self._z - other._z
        return Vector(x,y,z)

    def mult(self, factor):
        self._x = self._x * factor
        self._y = self._y * factor
        self._z = self._z * factor
        return self

    def __str__(self):
        return '%f,%f,%f' % (self._x, self._y, self._z)

class NBodySimulationBase(object):
    """Base class for an NBodySimulation"""

    def __init__(self, particles, start_time = 0):
        self.particles = particles
        self.time = start_time

    def calculate_energy(self):
        """Calculate the total energy of the particles"""
        T = 0
        U = 0

        for particle in self.particles:
            T += particle.kinetic_energy()
            for other_particle in self.particles:
                if particle != other_particle:
                    r = particle.pos() - other_particle.pos()
                    U -= 0.5 / r.mag()

        return T + U

    def run_simulation():
        pass
