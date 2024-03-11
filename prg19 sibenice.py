import random
def sibenice():

    slovo = random.choice(["opice" , "program" , "sibenice" , "mozek" , "leagueoflegends" , "monster" , "kopretina" ])
    pismena = 'abcdefghijklmnopqrstuvwxyz'
    pokus = 10
    guessmade = ''

    while len(slovo) > 0:
        main = ""
        missed = 0

        for letter in slovo:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == slovo:
            print(main)
            print("Vyhral jsi!")
            break

        print("Hadej slovo:" , main)
        guess = input()

        if guess in pismena:
            guessmade = guessmade + guess
        else:
            print("Napis pismeno")
            guess = input()

        if guess not in slovo:
            pokus = pokus - 1
            if pokus == 9:
                print("9 pokusu")
            if pokus == 8:
                print("8 pokusu")
                print("     O      ")
            if pokus == 7:
                print("7 pokusu")
                print("     O      ")
                print("     |      ")
            if pokus == 6:
                print("6 pokusu")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if pokus == 5:
                print("5 pokusu")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if pokus == 4:
                print("4 pokusy")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if pokus == 3:
                print("3 pokusy")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if pokus == 2:
                print("2 pokusy")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if pokus == 1:
                print("1 pokus")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if pokus == 0:
                print("Prohral jsi")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break

print("uhadni slovo, mas na to 10 pokusu")
sibenice()
print()