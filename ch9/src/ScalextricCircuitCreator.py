class ScalextricCircuitCreator:
    def get_max_section_circuit(self, pieces: tuple) -> int:
        S, C, D = pieces[0], pieces[1], pieces[2]
        if C <= 3:
            return 0
        if S + D == 0:
            return 4
        complex = (S > 1 or 0 < D < C) and C > 5
        used = 0
        C -= 4
        used += 4
        if complex:
            if S < 2:
                while C > 3:
                    C -= 4
                    used += 4
            else:
                while C > 1:
                    C -= 2
                    used += 2
        while S > 3:
            S -= 2
            used += 2
        while D > 1:
            D -= 2
            used += 2
        if S > 1 and D > 0:
            S -= 2; D -= 1
            used += 3
        if S > 1:
            S -= 2
            used += 2
        if D == 1 and complex:
            D -= 1
            used += 1
        return used
