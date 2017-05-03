class ITuentiChallengeSolver:
    def solve(self):
        arguments = self.readChallengeArguments()
        for i in range(len(arguments)):
            solution = self.solveChallenge(arguments[i])
            self.printChallengeSolution(i, solution)


    def readChallengeArguments(self) -> list: pass


    def solveChallenge(self, argument) -> int: pass


    def printChallengeSolution(self, case: int, solution): pass
