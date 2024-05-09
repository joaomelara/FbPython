import os

os.system('cls')
qtde= int(input("Digite o numero de habitantes : "))
HABITANTES = range(qtde)
salario = 0.00
total_salario = 0.00
numero_filhos = 0
total_filhos = 0
media_salarial = 0.00
media_filhos = 0.00
maior_salario = 0.00
percentual_salario_1000 = 0.00
contador_salario_1000 = 0

for pessoa in HABITANTES:
    print("Habitante ",(pessoa+1))
    salario = float(input("Digite o salario : "))
    numero_filhos = int(input("Digite o numero de filhos : "))

    total_salario = total_salario + salario
    total_filhos = total_filhos + numero_filhos
    
    if salario > maior_salario:
        maior_salario = salario
    
    if salario <= 1000:
        contador_salario_1000=contador_salario_1000+1


#calculo de medias
media_salarial = total_salario / qtde
media_filhos = total_filhos / qtde
percentual_salario_1000 = (contador_salario_1000 / qtde)*100

#saidas do programa
print("-"*60)
print(f"Total de salarios R$ {total_salario}")
print(f"Maior salario R$ {maior_salario}")
print(f"Media salarial R$ {media_salarial}")
print(f"Media de filhos : {media_filhos}")
print(f"Percentual de pessoas com salario até 1000 {percentual_salario_1000:.2f}%")

print("fim de programa")
