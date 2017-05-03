from ch11.ITuentiChallengeSolver import ITuentiChallengeSolver
from ch11.src.GalaxyPathSolver import GalaxyPathSolver


class Challenge11(ITuentiChallengeSolver):
    def __init__(self, inputFile, outputFile):
        self.input = open(inputFile, mode="r")
        self.output = open(outputFile, mode='w')


    def readChallengeArguments(self):
        cases = int(self.input.readline())
        arguments = []
        for i in range(cases):
            colors_length = int(self.input.readline())
            colors = self.read_colors(colors_length)
            galaxies_length = int(self.input.readline())
            galaxies = self.read_galaxies(galaxies_length)
            wormholes_length = int(self.input.readline())
            wormholes = self.read_wormholes(wormholes_length)
            arguments.append((colors, galaxies, wormholes))
        return arguments


    def read_colors(self, n):
        colors = {}
        for i in range(n):
            items = self.input.readline()[:-1].split(' ')
            colors[items[0]] = items[2:]
            if len(colors[items[0]]) == 0:
                colors[items[0]] = items[0]
        return colors


    def read_galaxies(self, n):
        galaxies = {}
        for i in range(n):
            colors_length = int(self.input.readline())
            colors = {}
            for j in range(colors_length):
                items = self.input.readline()[:-1].split(' ')
                colors[items[0]] = int(items[1])
            galaxies[i] = colors
        return galaxies


    def read_wormholes(self, n):
        wormholes = {}
        for i in range(n):
            items = self.input.readline().split(' ')
            origin = int(items[1])
            if origin not in wormholes:
                wormholes[origin] = []
            wormholes[origin].append((int(items[2]), items[0]))
        return wormholes


    def solveChallenge(self, argument):
        print(argument)
        galaxySolver = GalaxyPathSolver(argument[0], argument[1], argument[2])
        sols = []
        for i in range(len(argument[1])):
            sols.append(str(galaxySolver.get_min_distances(0, i)[1][0]))
        print(sols)
        return sols


    def printChallengeSolution(self, case, solution):
        self.output.write(f'Case #{case+1}: {" ".join(solution)}\n')
        print(f'Case #{case+1}: {" ".join(solution)}')
