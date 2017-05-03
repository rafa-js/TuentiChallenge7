class ITuentiChallengeSolver:
    def solve(self):
        arguments = self.readChallengeArguments()
        i = 0
        for argument in arguments:
            solution = self.solveChallenge(argument)
            self.printChallengeSolution(i, solution)
            i += 1


    def readChallengeArguments(self) -> list: pass


    def solveChallenge(self, argument) -> int: pass


    def printChallengeSolution(self, case: int, solution): pass
