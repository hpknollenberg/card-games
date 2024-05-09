import random


suits = ["clubs", "diamonds", "hearts", "spades"]
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

class Deck:
    def __init__(self, numb, suit, num_decks=1, deck=[]):
        self.numb = numb
        self.suit = suit
        self.num_decks = num_decks
        self.deck = deck
    
    def ask_num_decks(self):                                # This function asks the user for the number of decks.
        self.num_decks = input("How many decks? ")          # Then it checks to make sure the input is an integer between 1 and 10.
        if self.num_decks.isnumeric() == False:             # Finally, if all checks pass, it sets this turn's num_decks.
            print("Please enter an integer between 1 and 10.")
            self.ask_num_decks()
        elif int(self.num_decks) < 1:
            print("Please enter an integer between 1 and 10.")
            self.ask_num_decks()
        elif int(self.num_decks) > 10:
            print("Please enter an integer between 1 and 10.")
            self.ask_num_decks()
        else:
            self.num_decks = int(self.num_decks)
    
    def create(self):                                       # This function creates the deck based first on number of 
        for x in range(self.num_decks):                     # decks, then the suits, and then the numbers.
            for s in self.suit:
                for n in self.numb:
                    self.deck.append([n, s])

    def shuf(self):                                         # This function shuffles the deck.
        random.shuffle(self.deck)

    def draw(self):                                         # This function draws a card from the top of the deck.
        return self.deck.pop(0)
    
    def reset(self):
        del self.deck[:]
    
    
class Card:
    def __init__(self, card, value=0):
        self.card = card
        self.value = value

    def convert(self):                                      # This function converts the card into a number value.
        if self.card[0] == "A":
            self.value = 14
        elif self.card[0] == "K":
            self.value = 13
        elif self.card[0] == "Q":
            self.value = 12
        elif self.card[0] == "J":
            self.value = 11
        else:
            self.value = self.card[0]
    
    def convert_for_tie(self):                              # This function converts the card into a more complex number 
        if self.card[1] == "clubs":                         # value if needed for a tie.
            self.value = self.value
        elif self.card[1] == "diamonds":
            self.value = self.value * 2
        elif self.card[1] == "hearts":
            self.value = self.value * 3
        elif self.card[1] == "spades":
            self.value = self.value * 4

    def convert_blackjack(self): 
        self.value = 0                           #This function converts the cards into a number value for blackjack.
        ace = False
        for c in self.card:
            if c[0] == "A":
                self.value = self.value + 1
                ace = True
            elif c[0] == "K":
                self.value = self.value + 10
            elif c[0] == "Q":
                self.value = self.value + 10
            elif c[0] == "J":
                self.value = self.value + 10
            else:
                self.value = self.value + c[0]
        if ace == True:
            if self.value <= 11:
                self.value = self.value + 10
    

class Player:
    def __init__(self, name="Player", score=0, winnings=10, bet=0):             
        self.name = name
        self.score = score
        self.winnings = winnings
        self.bet = bet

    def win(self):                                          # This function keeps track of the scores.
        self.score = self.score + 1

    def name_input(self):                                   # This function keeps track of the player's name.
        self.name = input("What is your name? ")
        print ("You begin with 10 to wager.")

    def bet_input(self):                                    # This function keeps track of the player's bet.
        self.bet = input("How much do you wager? ")
        if self.bet.isnumeric() == False:                   
            print("Please enter an integer greater than or equal to 0.")
            self.bet_input()
        elif int(self.bet) > self.winnings:
            print("You cannot wager more than you have.")
            self.bet_input()
        else:
            self.bet = int(self.bet)

    def double_bet(self):                                   # This function is for when the player wins.
        self.winnings = self.winnings + self.bet

    def minus_bet(self):                                    # This function is for when the player loses.
        self.winnings = self.winnings - self.bet

    



def ask_play():
    if player_1.winnings > 0:
        play = input('Play high card or blackjack? H/B/Quit ')
        if play == "H":
            start_game()
        elif play == "B":
            start_blackjack()
        elif play == "Quit":
            pass
        else:
            print ("Please input either H, B, or Quit.")
            ask_play()
    else:
        print ("You lose.")


def start_game():
    deck_1 = Deck(numbers, suits)

    deck_1.ask_num_decks()
    deck_1.create()
    deck_1.shuf()

    player_1.bet_input()

    card_player = Card(deck_1.draw())
    card_dealer = Card(deck_1.draw())

    card_player.convert()
    card_dealer.convert()

    print (f"Your card: {card_player.card}")
    print (f"My card: {card_dealer.card}")

    

    def check_win():
        if card_player.value > card_dealer.value:
            print (f"{player_1.name} wins.")
            player_1.win()
            player_1.double_bet()
        elif card_player.value < card_dealer.value:
            print ("Dealer wins.")
            dealer.win()
            player_1.minus_bet()
        else:
            card_player.convert_for_tie()
            card_dealer.convert_for_tie()
            if card_player.value > card_dealer.value:
                print (f"{player_1.name} wins.")
                player_1.win()
                player_1.double_bet()
            elif card_player.value < card_dealer.value:
                print ("Dealer wins.")
                dealer.win()
                player_1.minus_bet()
            else:
                print ("Tie.")
        print(f"{player_1.name}'s wins: {player_1.score}")
        print(f"Dealer's wins: {dealer.score}")
        print(f"{player_1.name}'s winnings: {player_1.winnings}")
        deck_1.reset()
        ask_play()
    
    check_win()





def start_blackjack():
    deck_blackjack = Deck(numbers, suits)

    deck_blackjack.ask_num_decks()
    deck_blackjack.create()
    deck_blackjack.shuf()

    player_1.bet_input()

    hand_player = Card([deck_blackjack.draw()])
    hand_dealer = Card([deck_blackjack.draw()])
    hand_player.card.append(deck_blackjack.draw())
    hand_dealer.card.append(deck_blackjack.draw())
    
    hand_player.convert_blackjack()
    hand_dealer.convert_blackjack()

    print (f"Your cards: {hand_player.card}")
    print (f"My top card: {hand_dealer.card[1]}")

    def hit():
        hit_again = input("Hit? Y/N ")
        if hit_again == "Y":
            hand_player.card.append(deck_blackjack.draw())
            hand_player.convert_blackjack()
            print (f"Your cards: {hand_player.card}")
            print (f"My top card: {hand_dealer.card[1]}")
            if hand_player.value >= 21:
                pass
            else:
                hit()
        elif hit_again == "N":
            pass
        else:
            print ("Please enter either Y or N.")
            hit()

    hit()
    

    def dealer_turn():
        if hand_dealer.value < 17:
            hand_dealer.card.append(deck_blackjack.draw())
            hand_dealer.convert_blackjack()
            dealer_turn()
        else:
            pass

    dealer_turn()

    

    def check_win_blackjack():
        if hand_player.value > 21:
            print (f"Your cards: {hand_player.card}")
            print(f"Bust! Dealer wins.")
            dealer.win()
            player_1.minus_bet()
        elif hand_dealer.value > 21:
            print (f"Your cards: {hand_player.card}")
            print (f"My cards: {hand_dealer.card}")
            print (f"Dealer busts! {player_1.name} wins.")
            player_1.win()
            player_1.double_bet()
        elif hand_player.value > hand_dealer.value:
            print (f"Your cards: {hand_player.card}")
            print (f"My cards: {hand_dealer.card}")
            print (f"{player_1.name} wins.")
            player_1.win()
            player_1.double_bet()
        elif hand_player.value < hand_dealer.value:
            print (f"Your cards: {hand_player.card}")
            print (f"My cards: {hand_dealer.card}")
            print(f"Dealer wins.")
            dealer.win()
            player_1.minus_bet()
        else:
            print (f"Your cards: {hand_player.card}")
            print (f"My cards: {hand_dealer.card}")
            print("Tie!")
    
    check_win_blackjack()

    print(f"{player_1.name}'s wins: {player_1.score}")
    print(f"Dealer's wins: {dealer.score}")
    print(f"{player_1.name}'s winnings: {player_1.winnings}")

    deck_blackjack.reset()
    ask_play()





player_1 = Player()
dealer = Player()
player_1.name_input()
ask_play()







