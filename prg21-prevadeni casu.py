def prevod_hodin_na_dny_a_hodin(pocet_hodin):
  
  dny = pocet_hodin // 24
  hodiny = pocet_hodin % 24

  return {"dny": dny, "hodiny": hodiny}

pocet_hodin = int(input("Zadej počet hodin: "))

vysledek = prevod_hodin_na_dny_a_hodin(pocet_hodin)

print(f"{pocet_hodin} hodin je {vysledek['dny']} dní a {vysledek['hodiny']} hodin.")
