from card import Card
import random


class Board:
    """κλάση δημιουργίας του πίνακα του παιχνιδιού ανάλογα το επίπεδο 1,2,3"""

    colors = ['spade', 'club', 'heart', 'diamond']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, level):
        self.level = level
        self.cards = []
        if level == 3:
            end = 13
            start = 0
            self.columns = 13
        elif level == 2:
            start = 0
            end = 10
            self.columns = 10
        elif level == 1:
            start = 9
            end = 13
            self.columns = 4
        for color in Board.colors:
            for i in range(start, end):
                self.cards.append(Card(Board.values[i], color))

    def shuffle(self):
        return random.shuffle(self.cards)

    def hide(self):
        for card in self.cards:
            card.set_status(False)

    def reveal(self):
        for card in self.cards:
            card.set_status(True)

    def get_card(self, row, column):
        if not 1<= row <= 4 or not 1<= column <= self.columns:
            return None
        card = self.cards[(row - 1) * self.columns + column - 1]
        if not card.status:
            card.change_status()
            return card
        else:
            return None

    def is_complete(self):
        return [card.get_status() for card in self.cards].count(False) != 0

    def __str__(self):
        s = ''
        c = 0
        row = 1
        s += str(row) + '\t'
        first_line = '\t' + ''.join([str(i) + '\t' for i in range(1, self.columns + 1)]) + '\n'
        for item in self.cards:
            c += 1
            s += str(item) + '\t'
            if c % self.columns == 0:
                s += '\n'
                row += 1
                s += str(row) + '\t'
        s = first_line + s.rstrip()[:-1]
        return s.expandtabs(4)

    __repr__ = __str__


if __name__ == '__main__':
    b1 = Board(1)
    b1.shuffle()
    print(b1)
    b2 = Board(2)
    b2.shuffle()
    print(b2)
    b3 = Board(3)
    b3.shuffle()
    print(b3)
