import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_tally = 0
com_tally = 0
player_hand = []
com_hand = []
computer_wins = False
draw = False
player_wins = False

def final_score(final_player_hand, final_player_tally, final_com_hand, final_com_tally):
    print(f"Your final hand: {final_player_hand}, final score: {final_player_tally}")
    print(f"Computer's final hand: {final_com_hand}, final score: {final_com_tally}")

def com_draw(player_hand, player_tally, com_hand, com_tally):
    """function for computer to draw after first hand"""
    #pick new random card
    new_card = random.choice(cards)
    #rules for if card is 11 depending on outcome for dealer
    if new_card == 11:
        if com_tally + 11 >= 17 and com_tally + 11 <= 21:
            com_tally += 11
        elif com_tally + 11 > 21:
            com_tally += 1
    else:
        com_tally += new_card
    com_hand.append(new_card)
    #outcomes depending on new com_tally
    #no blackjack but computer's score is greater
    if com_tally > player_tally and com_tally <= 21:
        final_score(player_hand, player_tally, com_hand, com_tally)
        print("You lose 😤")
        computer_wins = True
        return
    #draw
    elif com_tally >= 17 and com_tally == player_tally:
        final_score(player_hand, player_tally, com_hand, com_tally)
        print("It's a draw 🙃")
        draw = True
        return
        # computer gets blackjack and has a greater score than user
    elif com_tally == 21 and com_tally > player_tally:
        final_score(player_hand, player_tally, com_hand, com_tally)
        print("Lose, opponent has Blackjack 😱")
        player_wins = True
        return
    #copmuter goes over 21
    elif com_tally > 21:
        final_score(player_hand, player_tally, com_hand, com_tally)
        print("Opponent went over. You win 😁")
        player_wins = True
        return
    elif com_tally >= 17 and com_tally < player_tally:
        final_score(player_hand, player_tally, com_hand, com_tally)
        print("You win 😃")
        player_wins = True
        return
    else:
        com_draw(player_hand, player_tally, com_hand, com_tally)

def first_hand_scores(com_card_1, player_hand, player_tally):
    """function to display current scores after the first hand is dealt"""
    print(f"Your cards: {player_hand}, current score: {player_tally}")
    print(f"Computer's first card: {com_card_1}")

def player_draw(player_tally, player_hand, com_card_1, com_hand, com_tally):
    """function for player to draw"""
    #at the first point the player has a tally and we will determine what to do depending on the card drawn
    #draw new card, add to player's hand
    new_card = random.choice(cards)
    player_hand.append(new_card)
    #rules for if card is 11 depending on outcome for dealer
    if new_card == 11:
        #if the value of the current tally plus 11 exeeds 21, 11 will instead be 1
        if player_tally + new_card > 21:
            player_tally += 1
        else:
            player_tally += new_card
    else:
        player_tally += new_card
    #rules depending on current tally
    #if player hits blackjack
    if player_tally == 21:
        final_score(player_hand, player_tally, com_hand, com_tally)
        print("Win with a blackjack!")
        player_wins = True
    #if player's score exceeds 21 after first new card dealt
    elif player_tally > 21:
        print(f"Your cards: {player_hand}, current score: {player_tally}")
        print(f"Computer's first card: {com_hand}")
        final_score(player_hand, player_tally, com_hand, com_tally)
        print("You went over. You lose 😭")
        computer_wins = True
        #if player's hand is under 21, show scores then offer choice to stick or twist
    else:
        print(f"Your cards: {player_hand}, current score: {player_tally}")
        print(f"Computer's first card: {com_card_1}")
        hit_or_stick = input("Type 'y' to get another card, type 'n' to pass").lower()
        #if stick, end function and and return updated player tally
        if hit_or_stick == 'n':
            com_draw(player_hand, player_tally, com_hand, com_tally)
        #if hit, function begins again
        elif hit_or_stick == 'y':
            player_draw(player_tally, player_hand, com_card_1, com_hand, com_tally)

def blackjack(player_tally, com_tally, player_hand, com_hand):
    #player is passed two cards, added to hand
    player_card_1 = random.choice(cards)
    player_card_2 = random.choice(cards)
    player_hand.extend([player_card_1, player_card_2])
    #computer passed one card, added to hand
    com_card_1 = random.choice(cards)
    com_hand.append(com_card_1)
    #tallies for player and computer are updated depending on value of cards
    #need to deal with edge case of two 11s being drawn
    if player_card_1 == 11 and player_card_2 == 11:
        player_tally += 12
    else:
        #if the value of the current tally plus 11 exeeds 21, 11 will instead be 1
        player_tally += player_card_1 + player_card_2
    com_tally += com_card_1
    #outcomes from first draw
    #outcome if player achieves Blackjack on first hand
    if player_tally == 21:
        first_hand_scores(player_card_1, player_card_2, com_card_1)
        final_score(player_hand, player_tally, com_hand, com_tally)
        print("Win with a blackjack 😎")
        player_wins = True
    else:
        print(f"Your cards: {player_hand}, current score: {player_tally}")
        print(f"Computer's first card: {com_hand}")
        #player decides to stick or twist after initial deal
        first_hit_or_stick = input("Type 'y' to get another card, type 'n' to pass:").lower()
        #if yes, the player draw function runds
        if first_hit_or_stick == "y":
            player_draw(player_tally, player_hand, com_card_1, com_hand, com_tally)
        #if no, go straight to the com_draw function
        elif first_hit_or_stick == "n":
            com_draw(player_hand, player_tally, com_hand, com_tally)
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n'.").lower()
    if play_again == "y":
        print("\n" * 2)
        player_tally = 0
        com_tally = 0
        player_hand = []
        com_hand = []
        blackjack(player_tally, com_tally, player_hand, com_hand)

print(art.logo)
play_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n'.").lower()
if play_or_not == "y":
    blackjack(player_tally, com_tally, player_hand, com_hand)













