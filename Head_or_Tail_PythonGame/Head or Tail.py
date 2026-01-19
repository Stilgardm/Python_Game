# bla bla
import random

print ("This is a game of head's and Tail")
answer = input ("Do you want to play (Y)es or (N)o?")
if answer.upper() != "Y" and answer.upper() != "N":
    #if answer not in ["Y", "N"]:
    print ("Please enter either Y or N")
    exit()
elif answer.upper() == "N":
    print ("Have a great day.")
    exit()
else:
    print ("Let's Play")

print("You get 10 chits")
i=10

while i>0:
    if i<2:
        MinimumBet=i
    else:
        MinimumBet=1

    print (f"You have now: {i} chits")
    BetValue = input (f"How much do you want to bet (1){MinimumBet}, (2)10% or (3)25%")

    if BetValue not in ["1", "2", "3", "4"]:
        print (BetValue)
        print ("Please enter either 1,2 or 3")
        continue
    elif BetValue == "2":
        HowMuchYouBet=0.1 * i
    elif BetValue == "3":
        HowMuchYouBet = 0.25 * i
    elif BetValue == "4":
        HowMuchYouBet = i
    else:
        HowMuchYouBet=MinimumBet

    print (f"you are betting {HowMuchYouBet}")

    while True:
        BetChoice = input ("(1)Head or (2)Tail")

        if BetChoice not in ["1", "2"]:
            print("Invalid choice! Please try again.")
            continue
        else:
            break

    target = random.randint(1, 2)
    if int(BetChoice) == 1 and int(BetChoice)==target:
        print(f"congratulation it is Head you won {HowMuchYouBet}")
        i=i+HowMuchYouBet
    elif int(BetChoice) == 2 and int(BetChoice)==target:
        print(f"congratulation it is Tail you won {HowMuchYouBet}")
        i=i+HowMuchYouBet
    else:
        print("sorry you lost")
        i=i-HowMuchYouBet

print ("Thank you for playing")





