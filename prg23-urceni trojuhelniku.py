def je_trojuhelnik(a, b, c):

  return (a + b > c) and (a + c > b) and (b + c > a)

a = int(input("Zadejte délku první strany: "))
b = int(input("Zadejte délku druhé strany: "))
c = int(input("Zadejte délku třetí strany: "))

if je_trojuhelnik(a, b, c):
  print("Jedná se o trojúhelník.")
else:
  print("Nejedná se o trojúhelník.")
