lista_muito_foda = []

while True:
    choice = int(input("1- Inserir Números\n2- Exibir Números\n3- Deletar Números\n4- Atualizar Números\n5- Sair\n"))

    if choice == 1:
        try:
            numero = int(input("Digite o novo item (número inteiro positivo): "))
            if numero > 0:
                lista_muito_foda.append(numero)
                print("Número adicionado de forma satisfatória, estilo quando você faz um combo muito foda em um videogame.")
            else:
                print("Por favor, digite um número inteiro positivo.")
        except ValueError:
            print("Por favor, digite um número inteiro positivo válido.")
            
    elif choice == 2:
        if not lista_muito_foda:
            print("A lista está vazia.")
        else:
            print("Itens na lista:")
            for item in lista_muito_foda:
                print(item)
        
            
    elif choice == 3:
        if not lista_muito_foda:
            print("A lista está vazia.")
        else:
            index = int(input("Digite o índice do item que deseja deletar: "))
            try:
                del lista_muito_foda[index]
                print("Item deletado com sucesso.")
            except IndexError:
                print("Índice inválido.")
                
    elif choice == 4:
        if not lista_muito_foda:
            print("A lista está vazia.")
        else:
            index = int(input("Digite o índice do item que deseja atualizar: "))
            try:
                novo_numero = int(input("Digite o novo valor: "))
                lista_muito_foda[index] = novo_numero
                print("Item atualizado.")
            except ValueError:
                print("Por favor, digite um número inteiro.")
            except IndexError:
                print("Índice inválido.")
                
    elif choice == 5:
        break
        
    else:
        print("Por favor, digite uma opção válida.")
