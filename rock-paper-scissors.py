import random

print "Welcome to Rock, Paper, Scissors! \nBest out of five wins! \nSelect your tool"
user_score = 0
computer_score = 0
def score():
    print "Current score \nUser: %d \nComputer:  %d" %(user_score, computer_score)

while True:

    user_pick = raw_input("Rock, paper or scissors? ").lower()
    options = ["rock","paper", "scissors"]
    computer_pick = random.choice(options)

    if user_pick == computer_pick:
        print "Both selected %s. Tie" %user_pick
    elif user_pick == "rock":
        if computer_pick == "scissors":
            print "Rock beats scissors. You win!"
            user_score += 1
            score()
        elif computer_pick == "paper":
            print "Paper bears rock. You lose."
            computer_score +=1
            score()
    elif user_pick == "paper":
        if computer_pick == "rock":
            print "Paper beats Rock. You win!"
            user_score += 1
            score()
        elif computer_pick == "scissors":
            print "Scissors beats paper. You Lose."
            computer_score +=1
            score()
    elif user_pick == "scissors":
        if computer_pick == "paper":
            print "scissors beats paper. You win!"
            user_score += 1
            score()
        elif computer_pick == "rock":
            print "Rock beats scissors. You lose."
            computer_score +=1
            score()
    if user_score == 3 or computer_score == 3 :
        break
            
if user_score == 3:
    print "You win!"
else:
    print "You lose."