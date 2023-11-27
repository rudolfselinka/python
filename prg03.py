známky = [[3, 1], [3, 2], [3, 1], [10, 3], [4, 4]]

# Inicializace proměnných pro celkovou váhu a vážený součet
celková_váha = 0
vážený_součet = 0

# Procházení každé dvojice váha, známka v seznamu
for váha, známka in známky:
    celková_váha += váha  # Přičítání váhy k celkové váze
    vážený_součet += váha * známka  # Přičítání váženého součtu

# Výpočet aritmetického průměru
aritmetický_průměr = vážený_součet / celková_váha

# Výpis výsledku
print("Aritmetický průměr:", aritmetický_průměr)