import random
playing=True
number=str(random.randint(10,20))
print("i am going to guess a no. between 10 till 20 and you have to guess that no.!!")
while playing:
    guess=input("Give your best guess!!")
    if number==guess:
        print("correct, you won the game")
        break
    else:
        print("Not quite right but you can still try again!")