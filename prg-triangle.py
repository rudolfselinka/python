h = 2
i = 1
while i <= h * 2:
    print("A"*i)
    i += 2

def triangl_1(h):
    for i in range(1, h + 1):
        print(" "*(h-i), "A"* (i*2 -1))

triangl_1 (40)