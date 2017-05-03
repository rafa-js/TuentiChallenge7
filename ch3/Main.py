import sys
import timeit

from ch3.src.Challenge3 import Challenge3


def main(inputFile='input.txt', outputFile='output.txt'):
    Challenge3(inputFile, outputFile).solve()


if __name__ == '__main__':
    if '--time' in sys.argv:
        print(timeit.timeit('main(sys.argv[1], sys.argv[2])', number=1, setup="from __main__ import main"))
    else:
        main(sys.argv[1], sys.argv[2])
