import sys

def main(args):
    pass

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=int, help='The number of bodies to simulate')
    args = parser.parse_args()

    sys.exit(main(args))
