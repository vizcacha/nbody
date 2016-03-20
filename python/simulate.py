import pygame

def main(args):
    fi = open(args.datafile, 'r')
    sys.exit()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('datafile', type=str, help='Output file from numerical code')
    args = parser.parse_args()
    main(args)
