from card import Card
from board import Board
from player import Player
from misc import *
from time import sleep

info()  # Δημιουργοί Παιχνιδιού
num_player = menu_player()  # Εμφάνιση μενού επιλογής παικτών
level = menu_level()  # Εμφάνιση μενού επιλογής επιπέδου
b = Board(level)  # Κατασκευή αντικειμένου board
b.shuffle()
print(b)
b.hide()
# Εισαγωγή ονομάτων παικτών
players = []
for player in range(num_player):
    name = input("Δώσε όνομα " + str(player + 1) + 'ου παίκτη : ')
    while name == '':
        name = input("Δώσε όνομα " + str(player + 1) + 'ου παίκτη : ')
    players.append(Player(name))
players.sort(key=lambda x: x.get_name())  # Ταξινόμηση λίστας παικτών αλφαβητικά
i = 0
while b.is_complete():
    c1 = move(b, players[i], 1)
    c2 = move(b, players[i], 2)
    s1 = c1.get_symbol()
    s2 = c2.get_symbol()
    points = match(c1, c2)
    nnext = (i + 1) % len(players)
    if points != 0:
        players[i].update_points(points)
        print("Επιτυχές ταίρισμα +", points, "πόντοι!", players[i].get_name(), "έχεις συνολικά ",
              players[i].get_points(),
              "πόντους")
        if s1 not in 'JK':
            i = nnext
        elif s1 == 'K':
            i = (i + 2) % len(players)

    else:
        if s1 in 'QK' and s2 in 'QK':
            c3 = move(b, players[i], 3)
            if match(c1, c3) != 0:
                points = match(c1, c3)
                players[i].update_points(points)
                print("Επιτυχές ταίρισμα +", points, "πόντοι!", players[i].get_name(), "έχεις συνολικά ",
                      players[i].get_points(), "πόντους")
                c2.set_status(False)
            elif match(c2, c3) != 0:
                points = match(c2, c3)
                players[i].update_points(points)
                print("Επιτυχές ταίρισμα +", points, "πόντοι!", players[i].get_name(), "έχεις συνολικά ",
                      players[i].get_points(), "πόντους")
                c1.set_status(False)
            else:
                print(b)
                c1.set_status(False)
                c2.set_status(False)
                c3.set_status(False)
                sleep(2)
        else:
            print(b)
            c1.set_status(False)
            c2.set_status(False)
            sleep(2)
        i = nnext
print("Πίνακας Βαθμολογίας")
print('-' * 40)
for i, player in enumerate(players):
    print(i + 1, player.get_name(), player.get_points())
print('-' * 40)
print('Νικητής είναι ο παίκτης ', max(players, key=lambda x: x.get_points()).get_name())
