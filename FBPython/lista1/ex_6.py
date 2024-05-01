import math


x1 = int(input("Leia o ponto: "))
y1 = int(input("Leia o ponto: "))
x2 = int(input("Leia o ponto: "))
y2 = int(input("Leia o ponto: "))


d = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

print(f"{d:.2f}")


