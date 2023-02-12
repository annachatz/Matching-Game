def info():
    print('-' * 40)
    print("Matching Game από")
    print('-' * 40)
    print("Άννα Χατζηπαπαδοπούλου p3200219\nΑιμίλιος Ντούκα p3200123\nΣταύρος Ζαχαρόπουλος p320052")
    print('-' * 40)


def menu_player():
    num_player = int(input("Δώσε αριθμό παικτών 1-5 : "))
    while not 1 <= num_player <= 5:
        print("Λάθος δεδομένα")
        num_player = int(input("Δώσε αριθμό παικτών 1-5 : "))
    return num_player


def menu_level():
    print("Επίπεδο Δυσκολίας")
    print(" 1 : Εύκολο")
    print(" 2 : Μέτριο")
    print(" 3 : Δύσκολο")
    level = int(input("Διάλεξε επίπεδο 1-3 : "))
    while not 1 <= level <= 3:
        print("Λάθος δεδομένα")
        level = int(input("Διάλεξε επίπεδο 1-3 : "))
    return level


def match(c1, c2):
    if c1.get_symbol() == c2.get_symbol():
        return c1.get_value()
    else:
        return 0


def move(b, p, count):
    print(b)
    while True:
        try:
            x, y = str(input(p.get_name() + " δώσε συντεταγμένες " + str(count) + "ου φύλλου x,y = ")).split()
        except:
            print('Προσοχή λάθος δεδομένα εισάγετε 2 ακεραίους με κενό')
        else:
            c = p.choose_card(b, int(x), int(y))
            if c is None:
                continue
            else:
                return c


