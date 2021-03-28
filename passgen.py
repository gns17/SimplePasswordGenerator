from random import choices, shuffle
from db import letters, symbols, numbers


class PassGen:

    def __init__(self):
        self.final_password = ""

    def generate_password(self, letter, symbol, number):
        ch_let = choices(letters, k=letter)
        ch_sym = choices(symbols, k=symbol)
        ch_num = choices(numbers, k=number)

        tl = ch_let + ch_num + ch_sym
        shuffle(tl)
        self.final_password = "".join(tl)

        return self.final_password
