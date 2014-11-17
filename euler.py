import sys
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

    def str(self):
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

    def str(self):
        return '%f,%f,%f' % (self._x, self._y, self._z)

def fromvectors(pos, vel):
    return Particle(pos._x, pos._y, pos._z, vel._x, vel._y, vel._z)

def calculate_force(particle, actor):
    """Calculate the force between two unit masses"""
    print 'Actor at %s' % actor.pos().str()
    print 'Particle at %s' % particle.pos().str()
    R = actor.pos() - particle.pos()
    print 'R = %s' % R.str()
    factor = 1.0 / R.mag() ** 3
    return R.mult(factor)

def take_timestep(particles, dt):
    newparticles = []

    for particle in particles:
        force = Vector(0.0,0.0,0.0)
        for actor in particles:
            if actor is not particle:
                force = force + calculate_force(particle, actor)
        newpos = particle.pos() + particle.velocity().mult(dt)
        newvel = particle.velocity() + force.mult(dt)
        newparticles.append( fromvectors(newpos, newvel) )
    return newparticles

def write_particles(particles, writer):
    for particle in particles:
        writer.write(particle.str())
        writer.write('\n')
    writer.write('<=== End of Timestep ===>\n')

def main(args):
    t = 0.0
    tfinal = 100.0
    dt = 0.1
    try:
        N = args.N
    except:
        N = 100 #TODO: Make the default more explicit and not in a try-except

    particles = [ Particle(random.random(),
                           random.random(),
                           random.random(),
                           random.random(),
                           random.random(),
                           random.random()) for i in xrange(N) ]
    fi = open('output', 'w')
    print 'Writing initial positions to output'
    write_particles(particles, fi)

    while t < tfinal:
        print 'Moving to time %f' % (t + dt)
        particles = take_timestep(particles, dt)
        t = t + dt
        print 'Writing new positions to file'
        write_particles(particles, fi)

    return 0


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=int, help='The number of bodies to simulate')
    args = parser.parse_args()

    sys.exit(main(args))
