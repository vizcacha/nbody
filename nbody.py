import sys

import common

def main(args):
    debug = args.debug

    if args.initial:
        initial_state = common.parse_initial_file(args.initial)

        if debug:
            for particle in initial_state:
                print particle

    elif args.N:
        initial_state = common.generate_initial_state(args.N)

        if debug:
            for particle in initial_state:
                print particle
    else:
        print 'Not enough information provided'

    return 0

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--initial', type=str, help='Text file containing initial conditions')
    parser.add_argument('--N', type=int, help='The number of bodies to simulate. They will be given random positions and velocities. Ignored if an initial file is provided.')
    parser.add_argument('--dt', type=float, help='The time step to take')
    parser.add_argument('--method', type=str, help='Integration scheme')
    parser.add_argument('--debug', help='Print debugging information to the console.')
    args = parser.parse_args()

    sys.exit(main(args))