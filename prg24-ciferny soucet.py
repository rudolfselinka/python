def cifernysoucet(cislo):
  
  soucet = 0
  while cislo > 0:
    zbytek = cislo % 10
    soucet += zbytek
    cislo //= 10

  return soucet
cislo = int(input("Zadejte číslo: "))

soucet = cifernysoucet(cislo)

print(f"Ciferný součet čísla {cislo} je {soucet}.")
