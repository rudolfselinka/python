import random

def generuj_nahodna_cisla(pocet):

  cisla = []
  for i in range(pocet):
    cisla.append(random.randint(1, 100))

  return cisla

def serad_pole(pole):

  for i in range(len(pole) - 1):
    for j in range(i + 1, len(pole)):
      if pole[i] > pole[j]:
        pole[i], pole[j] = pole[j], pole[i]

  return pole

pocet_cisel = 10

cisla = generuj_nahodna_cisla(pocet_cisel)
print(cisla)

serazena_cisla = serad_pole(cisla)
print(serazena_cisla)
