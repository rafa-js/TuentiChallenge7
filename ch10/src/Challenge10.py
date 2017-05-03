from ch10.ITuentiChallengeSolver import ITuentiChallengeSolver

from ch10.src.PasswordFinder import PasswordFinder


class Challenge10(ITuentiChallengeSolver):
    def __init__(self, inputFile, outputFile):
        self.passwordFinder = PasswordFinder('commits.txt')
        self.input = open(inputFile)
        self.output = open(outputFile, mode='w')


    def readChallengeArguments(self):
        cases = int(self.input.readline())
        arguments = []
        for i in range(cases):
            user, hist_size = self.input.readline().split(' ')
            history = []
            for i in range(int(hist_size)):
                date, times = self.input.readline().split(' ')
                history.append((date, int(times)))
            arguments.append((user, history))
        return arguments


    def solveChallenge(self, argument):
        return self.passwordFinder.find_password_for_user(argument[0], argument[1])


    def printChallengeSolution(self, case, solution):
        self.output.write(f'Case #{case+1}: {solution}\n')
        print(f'Case #{case+1}: {solution}')
