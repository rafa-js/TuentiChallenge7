class Tower:
    def __init__(self, F: int, S: int, shortcuts: list):
        self.Floors = F
        self.TotalShortCount = S
        self.Shortcuts = shortcuts


    def __repr__(self):
        return f'Tower(F:{self.Floors}, S:{self.TotalShortCount}, Shortcuts: {self.Shortcuts})'
