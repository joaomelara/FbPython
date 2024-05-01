C = int(input("Poe o codigo ae: " ))
N = int(input("Poe aszora ae: " ))

if (N>50):
    salarioBase = 50 * 10 
    HorasExtra = N - 50
    E = HorasExtra * 20
    salarioTotal = salarioBase+E
    print(salarioTotal)

else:
    salario = N*10
    print(salario)