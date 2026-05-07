import random


# ---------------- CARD CLASS ----------------
# Represents a single card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

# ---------------- DECK CLASS ----------------
# Represents a full deck of 52 cards
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]
        # Create all 52 cards
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    # Shuffle deck
    def shuffle(self):
        random.shuffle(self.cards)
    # Deal cards
    def deal(self, number_of_cards):
        dealt_cards = []
        for _ in range(number_of_cards):
            if len(self.cards) > 0:
                dealt_cards.append(self.cards.pop())
        return dealt_cards

# ---------------- HAND CLASS ----------------
# Represents player/dealer hand
class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.dealer = dealer
        self.value = 0
    # Add cards to hand
    def add_card(self, card_list):
        self.cards.extend(card_list)
    # Calculate hand value
    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True
        # Convert Ace from 11 → 1 if busted
        if has_ace and self.value > 21:
            self.value -= 10

    # Return current hand value
    def get_value(self):
        self.calculate_value()
        return self.value

    # Check blackjack
    def is_blackjack(self):
        return self.get_value() == 21

    # Display hand cards
    def display(self, show_all_dealer_cards=False):
        print(f"\n{'Dealer' if self.dealer else 'Player'} Hand:")
        for index, card in enumerate(self.cards):
            # Hide dealer first card initially
            if (
                index == 0
                and self.dealer
                and not show_all_dealer_cards
            ):
                print("Hidden Card")
            else:
                print(card)
        # Show player value
        if not self.dealer:
            print(f"Current Value: {self.get_value()}")
        print()

# ---------------- GAME CLASS ----------------
class Game:
    def play(self):
        game_number = 0
        games_to_play = 0
        # Input validation
        while games_to_play <= 0:
            try:
                games_to_play = int(
                    input("How many games do you want to play? ")
                )
            except ValueError:
                print("Please enter a valid number.")
        # Main game loop
        while game_number < games_to_play:
            game_number += 1
            # Create and shuffle deck
            game_deck = Deck()
            game_deck.shuffle()
            # Create hands
            player_hand = Hand()
            dealer_hand = Hand(dealer=True)
            # Initial dealing
            for _ in range(2):
                player_hand.add_card(game_deck.deal(1))
                dealer_hand.add_card(game_deck.deal(1))
            print("\n" + "=" * 35)
            print(f"BLACKJACK GAME {game_number}")
            print("=" * 35)
            player_hand.display()
            dealer_hand.display()
            # Check initial blackjack
            if self.check_winner(player_hand, dealer_hand):
                continue
            # ---------------- PLAYER TURN ----------------
            choice = ""
            while (
                player_hand.get_value() < 21
                and choice not in ["s", "stand"]
            ):
                choice = input(
                    "Choose Hit or Stand (h/s): "
                ).lower()
                while choice not in ["hit", "stand", "h", "s"]:
                    choice = input(
                        "Invalid choice. Enter h/s: "
                    ).lower()
                # Hit
                if choice in ["hit", "h"]:
                    player_hand.add_card(game_deck.deal(1))
                    player_hand.display()
            # Check after player turn
            if self.check_winner(player_hand, dealer_hand):
                continue
            # ---------------- DEALER TURN ----------------
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(game_deck.deal(1))
            dealer_hand.display(show_all_dealer_cards=True)
            # Final result
            print("Final Results:")
            print(f"Player Value: {player_hand.get_value()}")
            print(f"Dealer Value: {dealer_hand.get_value()}")
            self.check_winner(player_hand,dealer_hand,game_over=True)
        print("\nThanks for playing Blackjack!")

    # ---------------- WINNER LOGIC ----------------
    def check_winner(self,player_hand,dealer_hand,game_over=False):
        player_value = player_hand.get_value()
        dealer_value = dealer_hand.get_value()
        if not game_over:
            if player_value > 21:
                print("You busted! Dealer wins.")
                return True
            elif dealer_value > 21:
                print("Dealer busted! You win.")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Both have Blackjack! Draw.")
                return True
            elif player_hand.is_blackjack():
                print("Blackjack! You win.")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has Blackjack! Dealer wins.")
                return True
        else:
            if player_value > dealer_value:
                print("You win!")
            elif dealer_value > player_value:
                print("Dealer wins!")
            else:
                print("It's a draw!")
            return True

# ---------------- START GAME ----------------
game = Game()
game.play()