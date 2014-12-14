import sys

import common

def main(args):
    if args.initial:
        initial_state = common.parse_initial_file(args.initial)
        for particle in initial_state:
            print particle

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--initial', type=str, help='Text file containing initial conditions')
    parser.add_argument('--N', type=int, help='The number of bodies to simulate. They will be given random positions and velocities. Ignored if an initial file is provided.')
    parser.add_argument('--dt', type=float, help='The time step to take')
    parser.add_argument('--method', type=str, help='Integration scheme')
    args = parser.parse_args()

    sys.exit(main(args))