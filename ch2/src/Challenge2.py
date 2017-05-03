from ch2.ITuentiChallengeSolver import ITuentiChallengeSolver

from ch2.src.PythagorasJuniorHelper import BowlingScorer


class Challenge2(ITuentiChallengeSolver):
    def __init__(self, inputFile, outputFile):
        self.bowlingScorer = BowlingScorer()
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
        return self.bowlingScorer.getFramesFromRolls(argument)


    def printChallengeSolution(self, case, solution):
        self.output.write(f'Case #{case+1}: {" ".join(map(str, solution))}\n')
