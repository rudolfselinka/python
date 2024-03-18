import math

def o(r):

    print(round(2*math.pi*r, 0))
    r += 1
    print(round(2*math.pi*r, 0))
    return 
print(o(6378e3))