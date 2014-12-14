import sys
import math
import random

from common import Particle, Vector

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
