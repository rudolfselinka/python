import random
number = random.randrange(1,100)
guess = int(input("Typni si číslo: "))
while number!= guess:
    if guess < number:
        print("Zkus větší číslo")
        guess = int(input("Typni si znova: "))
    elif guess > number:
        print("Zkus menší číslo")
        guess = int(input("Typni si znova: "))
    else:
      break
print("Uhodl jsi to!")
