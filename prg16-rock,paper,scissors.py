import random

user_action = input("vyber si mezi kamenem, nůžkami a papírem ")
possible_actions = ["kámen", "nůžky", "papír"]
computer_action = random.choice(possible_actions)
print(f"\nvybíráš {user_action}, počítač vybírá {computer_action} \n")

if computer_action == user_action:
    print("REMIZOVAL JSI!")
elif user_action == "kámen":
    if computer_action == "nůžky":
        print("VYHRÁL JSI!")
    else:
        print("PROHRÁL JSI!")

elif user_action == "papír":
    if computer_action == "kámen":
        print("VYHRÁL JSI!")
    else:
        print("PROHRÁL JSI!")

elif user_action == "nůžky":
    if computer_action == "papír":
        print("VYHRÁL JSI!")
    else:
        print("PROHRÁL JSI!")
