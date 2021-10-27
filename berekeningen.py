# De user-defined functions
def addition(x,y):
    return x + y   

def substraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

def increment(x):
    return x + 1

def decrement(x):
    return x - 1

# De berekeningen
print('---------------')
print('10 + 12 = '+ str(addition(10,12)))
print('22 + 122 = '+ str(addition(22,122)))
print('14 + 58 = '+ str(addition(14,58)))
print('---------------')
print('58 - 34 = '+ str(substraction(58,34)))
print('568 - 245 = '+ str(substraction(568,245)))
print('254 - 57 = '+ str(substraction(254,57)))
print('---------------')
print('6 x 7 = '+ str(multiplication(6,7)))
print('25 x 5 = '+ str(multiplication(25,5)))
print('1258 x 745 = '+ str(multiplication(1258,745)))
print('---------------')
print('144 : 12 = '+ str(division(144,12)))
print('457 : 74 = '+ str(division(457,74)))
print('5 : 458 = '+ str(division(5,458)))
print('---------------')
print('12 + 1 = '+ str(increment(12)))
print('999 + 1 = '+ str(increment(999)))
print('47 + 1 = '+ str(increment(47)))
print('---------------')
print('34 - 1 = '+ str(decrement(34)))
print('146 - 1 = '+ str(decrement(146)))
print('77 - 1 = '+ str(decrement(77)))
