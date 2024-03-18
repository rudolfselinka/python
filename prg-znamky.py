znamky = [[4, 1], [6, 2], [3, 1], [10, 3], [8, 4]]

celkova_vaha = 0
vazeny_prumer_citatel = 0

for znamka in znamky:
    celkova_vaha += znamka[0]
    vazeny_prumer_citatel += znamka[0] * znamka[1] 

vazeny_prumer = vazeny_prumer_citatel / celkova_vaha

nevažený_průměr = sum(znamka[1] for znamka in znamky) /len(znamky)

rozdil = vazeny_prumer - nevažený_průměr

print(f"Celkový vážený průměr: {vazeny_prumer}")
print(f"Celkový nevážený průměr: {nevažený_průměr}")
print(f"Rozdíl mezi průměry: {rozdil}")