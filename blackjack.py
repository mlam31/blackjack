from random import shuffle
from time import sleep


def hand_result(hand):
    result = 0
    num_aces = 0
    
    for card in hand:
        if card.isdigit():
            result += int(card)
        elif card in ["J", "Q", "K"]:
            result += 10
        elif card == "A":
            num_aces += 1
            result += 11  # Ajoute 11 pour l'instant, on ajustera si nécessaire
    
    # Si le total avec tous les As comme 11 dépasse 21, ajuste les As à 1
    while result > 21 and num_aces > 0:
        result -= 10
        num_aces -= 1
    
    return result



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
        return self.cards.pop(0)
    
    def shuffle_deck(self):
        shuffle(self.cards)



class Player:
    def __init__(self, deck, balance=100):
        self.hand = []
        self.deck = deck
        players_list.append(self)

    def show_hand(self):
        print(f"Main du {self}: {self.hand} \n Résultat: {hand_result(self.hand)}" )
    
    def stand(self):
        """ Conserver ses cartes """
        pass

    def hit(self):
        """ Tirer une carte """
        card = deck.pop()
        self.hand.append(card)

    def double(self):
        """ Doubler la mise """
        pass

    def split(self):
        pass

class Croupier(Player):
    def __init__(self, deck, balance=100):
        super().__init__(deck, balance)

    def service(self):
        while hand_result(self.hand) <= 16:
            self.hit
        else:
            self.stand

    def show_hand_start(self):
        if len(self.hand) == 1:
            print(f"Main du Croupier: {self.hand[0]} \n Résultat: {hand_result(self.hand[0])}")
        else:
            print(f"Main du Croupier: {self.hand[0]} + ? \n Résultat: {hand_result(self.hand[0])} + ?")
        

class Game:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck

    def distribution(self):
        for _ in range(2):
            for player in self.players:
                sleep(2)
                player.hit()
                if isinstance(player, Croupier):
                    player.show_hand_start()
                else:
                    player.show_hand()
        

        
    
players_list = []

deck = Deck()


Joueur1 = Player(deck)
Crp = Croupier(deck)
print(f"La liste des joueurs est: {players_list}")


partie = Game(players_list, deck)
partie.distribution()
