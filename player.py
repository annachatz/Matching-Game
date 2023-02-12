from board import Board


class Player:
    """κλάση δημιουργίας παικτών του παιχνιδιού"""

    def __init__(self, name, points=0):
        self.name = name
        self.points = points

    def choose_card(self, board, x, y):
        card = board.get_card(x, y)
        return card

    def update_points(self, points):
        self.points += points

    def get_points(self):
        return self.points

    def get_name(self):
        return self.name


'''b1 = Board(1)
b1.shuffle()
print(b1)
p1 = Player('Tasos')
c1 = p1.choose_card(b1,3,2)'''
