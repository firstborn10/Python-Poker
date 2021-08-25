from poker import Deck, Hand


def add_cash():

    while True:
        try:
            cash = int(input("Hello! How much money would you like to add?: "))
            return cash
        except ValueError:
            print("Please input an valid number.")


def full_game(cash):
    # Defines payout
    payouts = {
        "Pair Jacks or Better": 1,
        "Two Pair": 2,
        "Three of a Kind": 3,
        "Straight": 4,
        "Flush": 6,
        "Full house": 9,
        "Four of a kind": 25,
        "Straight Flush": 50,
        "Royal flush": 800
    }

    while True:
        try:
            bet_size = int(input("How much would you like to bet?"))
            break
        except ValueError:
            print("Please enter a valid number.")

    cash -= bet_size

    user_hand = jacks_or_better()

    print(user_hand)

    if user_hand.rank == "High Card":
        print("You Lose")
        print("Current cash: " + str(cash))

    elif user_hand.rank == "Pair":
        if user_hand.sorted_by_frequency[0] < 11:
            print("You Lose.")
            print("Current cash: " + str(cash))
        else:
            print("You Win $" + str(bet_size) + "!")
            cash += bet_size
            print("Current cash: " + str(cash))

    else:
        print(user_hand.rank)
        print("You Win " + str(bet_size * payouts[user_hand.rank]))
        cash += bet_size * payouts[user_hand.rank]
        print("Current cash: " + str(cash))

    if input("Would you like to play again? y/n: ") == "y":
        full_game(cash)


def jacks_or_better():

    # Instantiates a new deck and shuffles it.
    deck = Deck()
    deck.new_deck()
    deck.shuffle()

    # Pulls five cards off "top" of deck to create user hand, then prints to console.
    user_hand = [deck.contents[0], deck.contents[1], deck.contents[2], deck.contents[3], deck.contents[4]]
    print(user_hand)

    # Simple function to break up a string by character.
    def split(word):
        return [char for char in word]

    # Prompts user to choose which cards to keep from initial hand and prints it out for user to see.
    # Also creates new hand to store kept cards.
    while True:
        try:
            cards_to_keep = split(input('Which cards would you like to keep?: '))
            break
        except ValueError:
            print("Please enter a unique combination of 1/2/3/4/5. ")

    print(cards_to_keep)
    new_hand = []

    for card in cards_to_keep:

        # If all 5 cards are kept, sends it to "Hand" class to rank.
        if len(cards_to_keep) == 5:
            print(Hand(user_hand).rank)
            break

        # If no cards are kept, new hand is made from top of deck.
        elif int(card) == 0:
            new_hand = [deck.contents[5], deck.contents[6], deck.contents[7], deck.contents[8], deck.contents[9]]
            print(Hand(new_hand).rank)

        # If a unique number of cards are kept, that card is appended to new list.
        if int(card) == 1:
            new_hand.append(user_hand[0])
        if int(card) == 2:
            new_hand.append(user_hand[1])
        if int(card) == 3:
            new_hand.append(user_hand[2])
        if int(card) == 4:
            new_hand.append(user_hand[3])
        if int(card) == 5:
            new_hand.append(user_hand[4])

    print(new_hand)

    # Adds new cards to new hand based on how many cards were kept.
    for x in range(5 - len(cards_to_keep)):
        new_hand.append(deck.contents[5 + x])
    return Hand(new_hand)


full_game(add_cash())
