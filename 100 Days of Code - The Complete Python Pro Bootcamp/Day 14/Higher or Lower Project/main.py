#Higher or Lower

#import necessary modules
import art
import random
import game_data

#function to print celebrity account data in readable format, compare follower counts and return account with more
def two_random_celebs(celeb_a, celeb_b):
    #print account info, extracting from data dictionary using f strings, as well as 'vs' art
    print(f"Compare A: {game_data.data[celeb_a]["name"]}, {game_data.data[celeb_a]["description"]} from {game_data.data[celeb_a]["country"]}")
    print(art.vs)
    print(f"Against B: {game_data.data[celeb_b]["name"]}, {game_data.data[celeb_b]["description"]} from {game_data.data[celeb_b]["country"]}")
    #check follower number of account A versus B, return "A" or "B" depending on which is higher
    if game_data.data[celeb_a]["follower_count"] > game_data.data[celeb_b ]["follower_count"]:
        return "A"
    else:
        return "B"

#game function
def higher_or_lower():
    #initiate user tally
    score = 0
    #create condition for game to end
    game_over = False

#initiate variables for two celebrity accounts using random integer that falls within range of size of dictionary
    celebrity_a = random.randint(0,49)
    celebrity_b = random.randint(0,49)
    # initiate while loop to avoid comparison of same celebrities
    while celebrity_b == celebrity_a:
        celebrity_b = random.randint(0, 49)
#initiate while loop to make game repeatable whilst user has guessed correctly
    while not game_over:
#skip 20 lines to create effect of new screen
        print("\n" * 20)
#print logo for game
        print(art.logo)
#only print updated score tally for user when there is a score to display
        if score != 0:
            print(f"You're right! Current score: {score}")
#initiate right answer variable which is the output of earlier function
        right_answer = two_random_celebs(celebrity_a, celebrity_b)

#take user answer from input
        answer = input("Who has more followers? Type 'A' or 'B': ")
#compare answer and user answer. If not same, game over
        if answer != right_answer:
            game_over = True
# compare answer and user answer. If same increase score by one, reassign celebrity B to be next celebB A
        elif answer == right_answer:
            score += 1
        celebrity_a = celebrity_b
#create condition for new celebrity b
        celebrity_b = random.randint(0,49)
# initiate while loop to avoid comparison of same celebrities
        while celebrity_b == celebrity_a:
            celebrity_b = random.randint(0, 49)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")


higher_or_lower()

