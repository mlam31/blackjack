from random import shuffle

def hand_result(hand):
    result = 0
    for carte in hand:
        if carte == "2":
            result += 2
        elif carte == "3":
            result += 3
        elif carte == "4":
            result += 4
        elif carte == "5":
            result += 5
        elif carte == "6":
            result += 6
        elif carte == "7":
            result += 7
        elif carte == "8":
            result += 8
        elif carte == "9":
            result += 9
        elif carte == "10":
            result += 10
        elif carte == "J":
            result += 10
        elif carte == "Q":
            result += 10
        elif carte == "K":
            result += 10
        elif carte == "A":
            result += 11
        else:
            pass
    return result

main = ["7", "5", "3"]
print(hand_result(main))
           


class Deck:
    def __init__(self):
        self.cards = []
        for _ in range(4*4):
            self.cards.append("A")
            self.cards.append("J")
            self.cards.append("Q")
            self.cards.append("K")
            for i in range(2, 11):
                self.cards.append(str(i))
        self.shuffle_deck()

    def show_cards(self):
        print(self.cards)

    def pop(self):
        """ Tire une carte du deck """
        return self.pop
    
    def shuffle_deck(self):
        shuffle(self.cards)


players_list = []

deck = Deck()
deck.show_cards()

class Player:
    def __init__(self, balance=100):
        self.main = []
        players_list.append(self)

    def stand(self):
        """ Conserver ses cartes """
        pass

    def hit(self):
        """ Tirer une carte """
        self.main.append(Deck.pop)

    def double(self):
        """ Doubler la mise """
        pass

    def split(self):
        pass

Joueur1 = Player()
print(players_list)

class Game:
    def __init__(self, joueurs, deck):
        self.joueurs = joueurs
        self.deck = deck

    def start_game(self):
        pass