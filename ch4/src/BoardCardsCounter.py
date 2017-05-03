class BoardCardsCounter:
    def get_required_cards(self, P: int) -> int:
        return P.bit_length()
