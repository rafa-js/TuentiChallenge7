from ch6.ITuentiChallengeSolver import ITuentiChallengeSolver
from ch6.src.ShortPathFinder import ShortPathFinder
from ch6.src.Tower import Tower


class Challenge6(ITuentiChallengeSolver):
    def __init__(self, inputFile, outputFile):
        self.requiredTablesSolver = ShortPathFinder()
        self.input = open(inputFile)
        self.output = open(outputFile, mode='w')


    def readChallengeArguments(self):
        cases = int(self.input.readline())
        arguments = []
        for i in range(cases):
            pair = self.input.readline().split(' ')
            F, S = int(pair[0]), int(pair[1])
            shortcuts = []
            for j in range(S):
                tuples = tuple(map(int, self.input.readline().split(' ')))
                shortcuts.append(tuples)
            arguments.append(Tower(F, S, shortcuts))
        return arguments


    def solveChallenge(self, argument: Tower):
        return self.requiredTablesSolver.find_shortest_path(argument)


    def printChallengeSolution(self, case, solution):
        self.output.write(f'Case #{case+1}: {solution}\n')
        print(f'Case #{case+1}: {solution}')
