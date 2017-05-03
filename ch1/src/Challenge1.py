from ch1.ITuentiChallengeSolver import ITuentiChallengeSolver
from ch1.src.RequiredPizzasSolver import RequiredPizzasSolver


class Challenge1(ITuentiChallengeSolver):
    def __init__(self, inputFile, outputFile):
        self.requiredTablesSolver = RequiredPizzasSolver()
        self.input = open(inputFile)
        self.output = open(outputFile, mode='w')


    def readChallengeArguments(self):
        cases = int(self.input.readline())
        arguments = []
        for i in range(cases * 2):
            line = self.input.readline()
            if i & 1 == 1:
                arguments.append(list(map(int, line.split(' '))))
        return arguments


    def solveChallenge(self, argument):
        total_slices = sum(argument)
        return self.requiredTablesSolver.getPizzasByPeople(total_slices)


    def printChallengeSolution(self, case, solution):
        self.output.write(f'Case #{case+1}: {solution}\n')
