from ch3.ITuentiChallengeSolver import ITuentiChallengeSolver
from ch3.src.BoardCardsCounter import BoardCardsCounter


class Challenge3(ITuentiChallengeSolver):
    def __init__(self, inputFile, outputFile):
        self.requiredTablesSolver = BoardCardsCounter()
        self.input = open(inputFile)
        self.output = open(outputFile, mode='w')


    def readChallengeArguments(self):
        cases = int(self.input.readline())
        arguments = []
        for i in range(cases):
            line = self.input.readline()
            arguments.append(int(line))
        return arguments


    def solveChallenge(self, argument):
        return self.requiredTablesSolver.get_required_cards(argument)


    def printChallengeSolution(self, case, solution):
        self.output.write(f'Case #{case+1}: {solution}\n')
