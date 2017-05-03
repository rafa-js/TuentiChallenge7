import unicodedata


class DataCleaner:
    def find_number(self, symbols: list) -> int:
        buffer = []
        i = 0
        while i < len(symbols):
            s = symbols[i]
            if self.is_number(s):
                if len(buffer) == 0:
                    while i < len(symbols) and self.is_number(symbols[i]):
                        buffer.append(self.to_number(symbols[i]))
                        i += 1
                else:
                    return None
            else:
                i += 1
                if not self.is_spacing(s):
                    return None
        n = int(''.join((str(b) for b in buffer))) if len(buffer) > 0 else None
        return n


    def is_spacing(self, s):
        return s == ' ' or unicodedata.category(s) == 'Zs'


    def to_number(self, s):
        return int(unicodedata.numeric(s))


    def is_number(self, s):
        return unicodedata.category(s) == 'Nd'
