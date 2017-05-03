from ch2.src.PythagorasJuniorHelper import PythagorasJuniorHelper
from ch4.ITuentiChallengeSolver import ITuentiChallengeSolver


class Challenge4(ITuentiChallengeSolver):
    def __init__(self, inputFile, outputFile):
        self.requiredTablesSolver = PythagorasJuniorHelper()
        self.input = open(inputFile)
        self.output = open(outputFile, mode='w')


    def readChallengeArguments(self):
        cases = int(self.input.readline())
        arguments = []
        for i in range(cases):
            items = self.input.readline().split(' ')
            arguments.append(list(map(int, items[1:])))
        return arguments


    def solveChallenge(self, argument):
        return self.requiredTablesSolver.getSmallestTrianglePerimeter(argument)


    def printChallengeSolution(self, case, solution):
        solution = 'IMPOSSIBLE' if solution is None else solution
        self.output.write(f'Case #{case+1}: {solution}\n')
