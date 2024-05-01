indice = float(input("Utilize sua ferramenta, informalmente chamada de teclada, para sobrepor os pixels em seu prompt de comando, para inserir os representativos numericos (sistema arabico) que te façam a vontade nesse recinto o qual emula a realidade ataves de receptores eletronicos: "))

if (indice<0.3 and indice>=0):
    print("O índice de poluição está dentre dos conformes ou próximo a eles, e não será necessário o fechamento de nenhum grupo")
elif(indice >= 0.3 and indice <0.4):
    print("O índice de poluição está alto, e será necessário o fechamento do primeiro grupo")
elif(indice >= 0.4 and indice < 0.5):
    print("O índice de poluição está alto, e será necessário o fechamento do primeiro e segundo grupo")
elif(indice >= 0.5):
    print("O índice de poluição está alto, e será necessário o fechamento de todos os grupos (primeiro, segundo e terceiro)")
else:
      print("Escreva um número plausível")



