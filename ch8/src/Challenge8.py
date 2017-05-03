from ch8.ITuentiChallengeSolver import ITuentiChallengeSolver
from ch8.src.DataCleaner import DataCleaner


class Challenge8(ITuentiChallengeSolver):
    def __init__(self, inputFile, outputFile):
        self.requiredTablesSolver = DataCleaner()
        self.input = open(inputFile, mode="r", encoding='utf-16')
        self.output = open(outputFile, mode='w')


    def readChallengeArguments(self):
        cases = int(self.input.readline())
        for i in range(cases):
            b = self.input.read(1)
            line = []
            while b != "\n":
                line.append(b)
                b = self.input.read(1)
            yield line


    def solveChallenge(self, argument):
        return self.requiredTablesSolver.find_number(argument)


    def printChallengeSolution(self, case, solution):
        formated_solution = 'N/A' if solution is None else format(solution, '0x')
        self.output.write(f'Case #{case+1}: {formated_solution}\n')
        print(f'Case #{case+1}: {formated_solution}')
