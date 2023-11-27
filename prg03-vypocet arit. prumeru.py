známky = [[3, 1], [3, 2], [3, 1], [10, 3], [4, 4]]
celková_váha = 0
vážený_součet = 0
for váha, známka in známky:
    celková_váha += váha 
    vážený_součet += váha * známka  
aritmetický_průměr = vážený_součet / celková_váha
print("Aritmetický průměr:", aritmetický_průměr)
