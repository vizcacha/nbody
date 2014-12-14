import math
import random

class Particle(object):
    """A single particle with unit mass"""

    def __init__(self, x, y, z, vx, vy, vz):
        self._x = x
        self._y = y
        self._z = z
        self._vx = vx
        self._vy = vy
        self._vz = vz

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
        return '%f,%f,%f,%f,%f,%f' % (self._x, self._y, self._z, self._vx, self._vy, self._vz)

    def pos(self):
        return Vector(self._x, self._y, self._z)

    def velocity(self):
        return Vector(self._vx, self._vy, self._vz)


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

def parse_initial_file(filename):
    """Read in the given file and parse its contents into a Particle list

    throws:
        IOError - File not readable
        FileFormatError - File has unexpected format

    """

    fi = open(filename, 'r')

    particles = []
    for line in fi.readlines():
        if line.strip():
            params = map(float, line.strip().split())
            if len(params) == 6:
                new_particle = Particle( params[0], params[1], params[2], params[3], params[4], params[5] )
                particles.append(new_particle)

    return particles

def generate_initial_state(count):
    """Generate an initial state for count particles

    Their positions and velocities will all be in the range 0,1
    """
    return [ Particle(random.random(),
                      random.random(),
                      random.random(),
                      random.random(),
                      random.random(),
                      random.random()) for i in xrange(count) ]