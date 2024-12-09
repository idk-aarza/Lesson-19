import random
options=["rock", "paper", "scissor"]
userchoice=input("chose  rock, paper,scissors")
computerchoice=random.choice(options)
if userchoice==computerchoice:
    print("it is a tie")
elif userchoice=="rock"and computerchoice=="scissors":
    print("rock beats scissors")
elif userchoice=="scissors"and computerchoice=="paper":
    print("scissors beats paper")
elif userchoice=="paper"and computerchoice=="rock":
    print("paper beats rock")
else: 
    ("you lose ")