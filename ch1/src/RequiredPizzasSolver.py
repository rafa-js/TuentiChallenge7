class RequiredPizzasSolver:
    SLICES_BY_PIZZA = 8


    def getPizzasByPeople(self, slices: int) -> int:
        if slices == 0:
            return 0
        pizzas = slices // self.SLICES_BY_PIZZA
        if slices & 7 > 0:
            pizzas += 1
        return pizzas
