class Card:
    """κλάση κατασκευής ενός φύλλου τράπουλας"""
    colors_dict = {'spade': 9824, 'club': 9827, 'heart': 9829, 'diamond': 9830}
    values_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                   'K': 10}

    def __init__(self, symbol, color, status=True):
        self.symbol = symbol
        self.color = color
        self.status = status

    def set_status(self, value):
        self.status = value

    def change_status(self):
        self.status = not self.status

    def get_symbol(self):
        return self.symbol

    def get_color(self):
        return self.color

    def get_status(self):
        return self.status

    def get_value(self):
        return Card.values_dict[self.symbol]

    def __str__(self):
        if self.status:
            return self.symbol + chr(Card.colors_dict[self.color])
        else:
            return 'X'

    __repr__ = __str__


if __name__ == '__main__':
    for color in Card.colors_dict:
        for value in Card.values_dict:
            c = Card(value, color)
            print(c, end=' ')
        print()
