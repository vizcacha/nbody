import sys
import math
import random

from common import *

class EulerSimulation(NBodySimulationBase):

    def __init__(self, particles, timestep, initial_time = 0):
        super(EulerSimulation, self).__init__(particles, initial_time)
        self.dt = timestep

    def run_simulation(self, endtime = 100):
        while self.time < endtime:
            self.particles = self.take_timestep()
            self.time += self.dt

    def take_timestep(self):
        newparticles = []

        for particle in self.particles:
            a = Vector(0.0,0.0,0.0)
            for actor in self.particles:
                if actor is not particle:
                    a = a + calculate_force(particle, actor)
            newpos = particle.pos() + particle.velocity().mult(self.dt)
            newvel = particle.velocity() + force.mult(self.dt)
            newparticles.append( particle_from_vectors(newpos, newvel) )
        return newparticles