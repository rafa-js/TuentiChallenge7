import math


class GalaxyPathSolver:
    def __init__(self, colors: dict, galaxies: dict, wormholes: dict):
        self.colors = colors
        self.galaxies = galaxies
        self.wormholes = wormholes


    def get_min_distances(self, start, end) -> list:
        opened = {start: (start, {})}
        while opened:
            v, state = opened.popitem()
            spent_time, colors = state
            if end == v:
                return [v, state, spent_time]
            for wormhole in self.get_possible_wormholes(v, state):
                new_colors = set(list(colors) + list(wormhole[2]))
                wormhole_color = wormhole[3]
                spent_time = spent_time + max([self.galaxies[v][c] for c in wormhole_color])
                if wormhole_color in new_colors:
                    new_colors.remove(wormhole_color)
                opened[wormhole[0]] = (spent_time + new_colors)
        return [start, [], -1]


    def get_possible_wormholes(self, v, state) -> list:
        wormholes = []
        spent_time, colors = state
        for wormhole in self.wormholes[v]:
            dest, color = wormhole
            if color in colors or all([c in colors for c in self.colors[color]]):
                ccc = sorted([(c, self.galaxies[v][c]) for c in self.galaxies[v]],
                             reverse=True)
                wormholes.append((dest, 0, [color], color))

                for cw in ccc:
                    c, w = cw
                    recharged_colors = set([a for a in self.galaxies[v]])
                    wormholes.append((dest, w, recharged_colors, color))
            elif color in self.galaxies[v]:
                recharged_colors = set([c for c in self.galaxies[v]])
                wormholes.append((dest, self.galaxies[dest][color], recharged_colors, color))
        return sorted(wormholes, key=lambda w: w[1])
