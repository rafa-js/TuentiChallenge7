import math


class PythagorasJuniorHelper:
    def getSmallestTrianglePerimeter(self, sides: list) -> int:
        sides.sort()
        min_perimeter = math.inf
        for i in range(len(sides)):
            a = sides[i]
            for j in range(i + 1, len(sides)):
                b = sides[j]
                if a + b < min_perimeter:
                    for k in range(j + 1, len(sides)):
                        c = sides[k]
                        perimeter = a + b + c
                        if perimeter < min_perimeter:
                            min_perimeter = perimeter if a - b < c < a + b else min_perimeter
                        else:
                            break
                else:
                    break

        return None if min_perimeter == math.inf else min_perimeter
