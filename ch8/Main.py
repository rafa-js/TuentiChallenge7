import sys
import timeit

from ch8.src.Challenge8 import Challenge8


def main(inputFile='input.txt', outputFile='output.txt'):
    Challenge8(inputFile, outputFile).solve()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Please, provide the system arguments input_file and output_file')
        exit(-1)
    if '--time' in sys.argv:
        print(timeit.timeit('main(sys.argv[1], sys.argv[2])', number=1, setup="from __main__ import main"))
    else:
        main(sys.argv[1], sys.argv[2])
