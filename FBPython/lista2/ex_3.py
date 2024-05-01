import math

num1 = int(input("Poe o numero 1: "))
num2 = int(input("Poe o numero 2: "))
num3 = int(input("Poe o numero 3: "))
num4 = int(input("Poe o numero 4: "))

a = math.pow(num1,2)
b = math.pow(num2,2)
c = math.pow(num3,2)
d = math.pow(num4,2)

if(c >=1000):
    print(c)
else:
    print(f"{num1}:{a}\n{num2}:{b}\n{num3}:{c}\n{num4}:{d}")