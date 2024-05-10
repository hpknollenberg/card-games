import random
import os


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
    
    def reset(self):                                        # This function empties the deck.
        del self.deck[:]
    
    
class Card:
    def __init__(self, card, turn=0, value=0):
        self.card = card
        self.value = value
        self.turn = turn

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

    def convert_war(self):
        self.value = 0
        if self.card[0][0] == "A":
            self.value = 14
        elif self.card[0][0] == "K":
            self.value = 13
        elif self.card[0][0] == "Q":
            self.value = 12
        elif self.card[0][0] == "J":
            self.value = 11
        else:
            self.value = self.card[0][0]

    def discard(self):
        return self.card.pop(0)

    def reset(self):
        del self.card[:]

    def turn_counter(self):
        self.turn = self.turn + 1
    

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

    



def ask_play():                                                     # This function, if the player has money to wager, asks the player
    if player_1.winnings > 0:                                       # which game they want to play. If they don't have any money, then
        play = input('Play high card, blackjack, or war? H/B/W/Quit ')      # they lose.
        if play == "H":
            start_game()
        elif play == "B":
            start_blackjack()
        elif play == "W":
            start_war()
        elif play == "Quit":
            pass
        else:
            print ("Please input either H, B, W, or Quit.")
            ask_play()
    else:
        print ("You lose.")



def start_game():                                                   # This function creates and shuffles the deck. Then it deals cards
    deck_1 = Deck(numbers, suits)                                   # to each player after asking the user for their bet. It also runs
                                                                    # the convert function to convert the cards into numerical values.
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

    

    def check_win():                                                # This function compares the values of each player's card.
        if card_player.value > card_dealer.value:                   # Whoever's is highest, wins.
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


def start_blackjack():                                              # This function begins very similar to start_game, but goes on to
    deck_blackjack = Deck(numbers, suits)                           # run blackjack rather than highcard.

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

    def hit():                                                      # This function asks the player if they want another card.
        hit_again = input("Hit? Y/N ")                              # It also evaluates whether or not they've gone over 21.
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
    

    def dealer_turn():                                              # This function evaluates whether the dealer has hit 17. If not,
        if hand_dealer.value < 17:                                  # then they draw another card.
            hand_dealer.card.append(deck_blackjack.draw())
            hand_dealer.convert_blackjack()
            dealer_turn()
        else:
            pass

    dealer_turn()

    

    def check_win_blackjack():                                      # This function checks to see if the player or the dealer has gone
        if hand_player.value > 21:                                  # over 21. It also compares each player's scores to one another.
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


def start_war():
    deck_war = Deck(numbers, suits)

    deck_war.create()
    deck_war.shuf()

    player_1.bet_input()

    hand_player = Card([deck_war.draw()])
    hand_dealer = Card([deck_war.draw()])
    for x in range(25):
        hand_player.card.append(deck_war.draw())
        hand_dealer.card.append(deck_war.draw())
    
    discard_pile = Card([])

    
    def play_war():
        if len(hand_player.card) == 52:                                   # If player has 52 cards, then they win.
            print (f"{player_1.name} wins.")
            player_1.win()
            player_1.double_bet()
            print(f"{player_1.name}'s wins: {player_1.score}")
            print(f"Dealer's wins: {dealer.score}")
            print (f"{player_1.name}'s winnings: {player_1.winnings}")
        elif len(hand_dealer.card) == 52:                                 # If dealer has 52 cards, then they win.
            print ("Dealer wins.")
            dealer.win()
            player_1.minus_bet()
            print(f"{player_1.name}'s wins: {player_1.score}")
            print(f"Dealer's wins: {dealer.score}")
            print (f"{player_1.name}'s winnings: {player_1.winnings}")
        else:
            if hand_player.turn < 900:                                    # Caps the amount of turns to 900 to avoid recursion error.
                hand_player.turn_counter()
                print (f"turn: {hand_player.turn}")
                try:
                    print (f"player: {hand_player.card[0]}")
                except:
                    pass

                try: 
                    print (f"dealer: {hand_dealer.card[0]}")
                except:
                    pass
                
                def turn():
                    try:                                                  # Check to see if player has a card, then converts it to a value
                        hand_player.convert_war()                         # and then puts it in the discard pile.
                        discard_pile.card.append(hand_player.discard())
                    except:
                        print ("You ran out of cards.")                    # If player runs out of cards, then dealer gets the discard pile.
                        hand_dealer.card.extend(discard_pile.card) 
                        return
                        
                    try:
                        hand_dealer.convert_war()                          # Check to see if dealer has a card, then converts it to a value
                        discard_pile.card.append(hand_dealer.discard())    # and then puts it in the discard pile.
                    except:
                        print ("Dealer ran out of cards.")                 # If dealer runs out of cards, then player gets the discard pile.
                        hand_player.card.extend(discard_pile.card)
                        return

                    if hand_player.value > hand_dealer.value:              # If player card value is greater than dealer card value then
                        hand_player.card.extend(discard_pile.card)         # player gets the discard pile.
                        discard_pile.reset()
                    elif hand_player.value < hand_dealer.value:            # If dealer card value is greater than dealer card value then
                        hand_dealer.card.extend(discard_pile.card)         # dealer gets the discard pile.
                        discard_pile.reset()
                    else:
                        for x in range(3):                                 # WAR
                            try:
                                print (f"player: {hand_player.card[0]}")
                                discard_pile.card.append(hand_player.discard())  # Check to see if player has a card. If so, puts it in the 
                            except:                                              # discard pile.
                                break
                                
                            try:
                                print (f"dealer: {hand_dealer.card[0]}")  
                                discard_pile.card.append(hand_dealer.discard())  # Check to see if dealer has a card. If so, puts it in the                                                                               
                            except:                                              # discard pile.                
                                break
                turn()
                play_war()
            else:
                print("Game too long. You tie.")
                
    
    play_war()
    ask_play()

        





player_1 = Player()                         #Asks the player for their name, and then runs the ask_play function.
dealer = Player()
player_1.name_input()
ask_play()