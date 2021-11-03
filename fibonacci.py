x = 1
y = 0
o = 0
def fibonacci(nummer1,nummer2):
    z = x + y
    return z
while o < 23:
    print(fibonacci(x,y))
    z = fibonacci(x,y)
    y = x
    x = z
    o += 1

