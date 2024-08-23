from random import shuffle


class Deck:
    def __init__(self):
        self.cartes = []
        for _ in range(4*4):
            self.cartes.append("A")
            self.cartes.append("J")
            self.cartes.append("Q")
            self.cartes.append("K")
            for i in range(2, 11):
                self.cartes.append(str(i))
        self.shuffle_deck()

    def show_cartes(self):
        print(self.cartes)

    def pop(self):
        """ Tire une carte du deck """
        return self.pop
    
    def shuffle_deck(self):
        shuffle(self.cartes)


liste_joueurs = ["Croupier"]

deck = Deck()
deck.show_cartes()
