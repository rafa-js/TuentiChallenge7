from ch9.ITuentiChallengeSolver import ITuentiChallengeSolver
from ch9.src.ScalextricCircuitCreator import ScalextricCircuitCreator


class Challenge9(ITuentiChallengeSolver):
    def __init__(self, inputFile, outputFile):
        self.circuitCreator = ScalextricCircuitCreator()
        self.input = open(inputFile, mode="r")
        self.output = open(outputFile, mode='w')


    def readChallengeArguments(self):
        cases = int(self.input.readline())
        arguments = []
        for i in range(cases):
            items = self.input.readline().split(' ')
            arguments.append(list(map(int, items)))
        return arguments


    def solveChallenge(self, argument):
        return self.circuitCreator.get_max_section_circuit(argument)


    def printChallengeSolution(self, case, solution):
        self.output.write(f'Case #{case+1}: {solution}\n')
        print(f'Case #{case+1}: {solution}')
