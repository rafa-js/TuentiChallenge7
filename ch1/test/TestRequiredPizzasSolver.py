import unittest

from ch1.src.RequiredPizzasSolver import RequiredPizzasSolver


class TestRequiredPizzasSolver(unittest.TestCase):
    def setUp(self):
        self.solver = RequiredPizzasSolver()


    def testFourPeople(self):
        solution = self.solver.getPizzasByPeople(4)
        self.assertEqual(solution, 1)


    def testTwoPeople(self):
        solution = self.solver.getPizzasByPeople(8)
        self.assertEqual(solution, 1)


    def testFivePeople(self):
        solution = self.solver.getPizzasByPeople(9)
        self.assertEqual(solution, 2)


    def testEightPeople(self):
        solution = self.solver.getPizzasByPeople(81)
        self.assertEqual(solution, 11)


    def testSevenSevenSevenSevenSevenPeople(self):
        solution = self.solver.getPizzasByPeople(77777)
        self.assertEqual(solution, 9723)


    def testMaximumPeople(self):
        solution = self.solver.getPizzasByPeople(10000 * 100)
        self.assertEqual(solution, 125000)


if __name__ == '__main__':
    unittest.main()
