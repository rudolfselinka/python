questions = ("Kolik planet je ve slunecni soustave?: ",
                       "Kolik je rocnich obdobi?: ",
                       "Je IT obor zabavny?: ",
                       "Kolik existuje pohlavi?: ")

options = (("A. 7", "B. 8", "C. 9", "D. 6"),
                   ("A. 2", "B. 5", "C. 3", "D. 4"),
                   ("A. ne", "B. mozna", "C. ano", "D. je super, nejlepsi, uzasnej"),
                   ("A. 2", "B. 3", "C. 68", "D. 135"))

answers = ("B", "D", "D", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Vyber si (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("SPRAVNE")
    else:
        print("SPATNE")
        print(f"{answers[question_num]} je spravna odpoved")
    question_num += 1

print("Vysledky")

print("odpovedi: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("tipy: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Tvoje score je: {score}%")