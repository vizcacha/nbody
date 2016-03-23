import sys

from common import Particle, Vector

EXECUTION_SUCCESSFUL = 0
INSUFFICIENT_USER_INFORMATION = 1

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
            if len(params) == 7:
                new_particle = Particle(params[0], params[1], params[2], params[3], params[4], params[5], params[6])
                particles.append(new_particle)

    return particles


def generate_initial_state(count):
    """Generate an initial state for count particles of identical unit mass

    Their positions and velocities will all be in the range 0,1
    """
    return [ Particle(random.random(),
                      random.random(),
                      random.random(),
                      random.random(),
                      random.random(),
                      random.random()) for i in xrange(count) ]


def main(args):
    debug = args.debug

    if args.initial:
        initial_state = parse_initial_file(args.initial)
    elif args.N:
        initial_state = common.generate_initial_state(args.N)
    else:
        print 'Not enough information provided'
        return INSUFFICIENT_USER_INFORMATION

    if debug:
        for particle in initial_state:
            print particle

    method = args.method.lower()
    if method == 'euler':
        # Create an Euler evolution
        from euler import EulerSimulation
        simulation = EulerSimulation(initial_state, dt)
    elif method == 'rk4':
        # Create a fourth-order Runge-Kutta evolution
    else:
        print 'No or unknown method specified.'
        return INSUFFICIENT_USER_INFORMATION

    #TODO: Parse out the number of steps to take
    simulation.run_simulation()

    return EXECUTION_SUCCESSFUL

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--initial', type=str, help='Text file containing initial conditions')
    parser.add_argument('--N', type=int, help='The number of bodies to simulate. They will be given random positions and velocities. Ignored if an initial file is provided.')
    parser.add_argument('--steps', type=int, help='The number of steps to take')
    parser.add_argument('--dt', type=float, help='The time step to take')
    parser.add_argument('--method', type=str, help='Integration scheme')
    parser.add_argument('--debug', help='Print debugging information to the console.')
    args = parser.parse_args()

    sys.exit(main(args))
