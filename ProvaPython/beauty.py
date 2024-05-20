import time
import pymysql
from Classe import ProdutoBeleza 
from Classe import Usuario

con = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='beautystore'
)

carrinho = []

print("1 - CADASTRAR USER")
print("2 - CADASTRAR PRODUTO")
print("3 - MOVIMENTAR")
print("4 - SAIR")

op = input("Qual é a opção? ")

while op != "4":

    if op == "1":
            while True:
                with con.cursor() as cursor:
                    TABLE_NAME = "USUARIO"
                    cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
                                   'ID INT AUTO_INCREMENT PRIMARY KEY ,'
                                   'EMAIL VARCHAR(50) ,'
                                   'SENHA VARCHAR(50) '
                                   ')')
                    con.commit()

                    with con.cursor() as cursor:
                        print("1 - CADASTRAR")
                        print("2 - ALTERAR")
                        print("3 - LISTAR")
                        print("4 - EXCLUIR")
                        print("5 - SAIR")
                        opc = input("Escolha uma opção: ")

                        if opc == '5':
                            time.sleep(2)
                            print("Até Breve...")
                            break

                        elif opc == '1':
                            print("-" * 20)
                            print("CADASTRAMENTO")
                            email = input('Digite o email: ')
                            senha = input("Digite a senha: ")
                            item = Usuario(email, senha)
                            cursor.execute(f'INSERT INTO USUARIO (EMAIL, SENHA)'
                                           'VALUES (%s, %s)', (item.email, item.senha))
                            con.commit()
                            print('USUARIO CADASTRADO')
                            time.sleep(2)

                        elif opc == '2':
                            print("-"*20)
                            print("ALTERAÇÃO")
                            email = input("Digite o email do user a ser modificado: ")
                            
                            senha = input("Informe a nova senha: ")
                            item = Usuario(email,senha)
                            cursor.execute('UPDATE USUARIO SET SENHA=%s WHERE EMAIL=%s', (item.senha, item.email))
                            con.commit()
                            print('USUARIO ALTERADO')
                            time.sleep(2)

                        elif opc == '3':
                            print("-" * 20)
                            print("LISTAGEM")
                            cursor.execute("SELECT * FROM USUARIO")
                            resposta = cursor.fetchall()
                            for linha in resposta:
                                print(linha)
                            time.sleep(3)

                        elif opc == '4':
                            print("-" * 20)
                            print("DELETE")
                            email = input("Digite o email do usuário a ser deletado: ")
                            cursor.execute("DELETE FROM USUARIO WHERE EMAIL = %s", (email,))
                            con.commit()
                            print("Usuário deletado...")
                            time.sleep(1)

    elif op == '2':
            while True:
                with con.cursor() as cursor:
                    TABLE_NAME = "produtobeleza"
                    cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
                                'id_produtobeleza INT AUTO_INCREMENT PRIMARY KEY ,'
                                'CODIGO VARCHAR(50) ,'
                                'DESCRICAO VARCHAR(50) ,'
                                'MARCA VARCHAR(50) ,'
                                'VALOR DOUBLE(10,2) ,'
                                'ESTOQUE INT NOT NULL'  
                    ')')
                    con.commit()


                    with con.cursor() as cursor:

                        print("1 - CADASTRAR")
                        print("2 - ALTERAR")
                        print("3 - LISTAR")
                        print("4 - EXCLUIR")
                        print("5 - SAIR")
                        opc = input("Escolha uma opção: ")

                        if opc == '5':
                            time.sleep(2)
                            print("Até Breve...")
                            break

                        elif opc == '1':
                            print("-" * 20)
                            print("CADASTRAMENTO")
                            codigo = input("Digite o código do produto: ")
                            descricao = input('Digite a descrição/nome: ')
                            marca = input("Digite a marca: ")
                            valor = float(input("Digite o valor do produto : R$ "))
                            estoque = int(input("Digite o valor do estoque: "))
                            item = ProdutoBeleza(codigo, descricao, marca, valor, estoque)
                            if item.adicionar_estoque(estoque):
                                cursor.execute('INSERT INTO produtobeleza (CODIGO, DESCRICAO, MARCA, VALOR, ESTOQUE) VALUES (%s, %s, %s, %s, %s)',
                                            (item.codigo, item.descricao, item.marca, item.valor, item.estoque))
                                con.commit()
                                print('PRODUTO CADASTRADO')
                            else:
                                print('Quantidade de estoque inválida. Deve ser entre 1 e 30.')
                            time.sleep(2)

                        elif opc == '2':
                            print("-" * 20)
                            print("ALTERAÇÃO")
                            codigo = input("Digite o código do produto a ser modificado: ")
                            descricao = input("Informe a nova descrição do produto: ")
                            valor = float(input("Informe o novo valor do produto: "))
                            quantidade = int(input("Informe a quantidade de estoque a ser adicionada: "))

                            with con.cursor() as cursor:
                                cursor.execute('SELECT ESTOQUE FROM PRODUTOBELEZA WHERE CODIGO=%s', (codigo,))
                                produto = cursor.fetchone()
                                
                                if produto:
                                    estoque_atual = produto[0]
                                    item = ProdutoBeleza(codigo, descricao, '', valor, estoque_atual)
                                    
                                    if item.adicionar_estoque(quantidade):
                                        cursor.execute('UPDATE PRODUTOBELEZA SET DESCRICAO=%s, VALOR=%s, ESTOQUE=%s WHERE CODIGO=%s',
                                                    (descricao, valor, item.estoque, codigo))
                                        con.commit()
                                        print("PRODUTO ALTERADO COM SUCESSO")
                                    else:
                                        print('Quantidade de estoque inválida. Deve ser entre 1 e 30.')
                                else:
                                    print('Produto não encontrado.')
                            time.sleep(2)


                        elif opc == '3':
                            print("-" * 20)
                            print("LISTAGEM")
                            with con.cursor() as cursor:
                                cursor.execute("SELECT * FROM produtobeleza")
                                resposta = cursor.fetchall()
                                for linha in resposta:
                                    print(linha)
                                time.sleep(3)

                        elif opc == '4':
                            print("-" * 20)
                            print("DELETE")
                            codigo = input("Digite o código do produto a ser deletado: ")
                            with con.cursor() as cursor:
                                cursor.execute("DELETE FROM produtobeleza WHERE CODIGO = %s", (codigo,))
                                con.commit()
                                print("Produto deletado...")
                                time.sleep(1)
    
    elif op == "3":
         with con.cursor() as cursor:
                        TABLE_NAME = "USUARIO"
                        email = (input("Digite o email da conta: "))
                        senha = (input("Digite o senha da conta: "))
                        
                        # Verificar se a conta existe
                        sql_verificar_conta = f'SELECT * FROM {TABLE_NAME} WHERE email = %s AND senha = %s'
                        cursor.execute(sql_verificar_conta, (email,senha))
                        conta = cursor.fetchone()

                        if conta:
                            with con.cursor() as cursor:
                                TABLE_NAME = "produtobeleza"
                                cursor.execute(f"SELECT * FROM {TABLE_NAME}\n\n")
                                resposta = cursor.fetchall()
                                for linha in resposta:
                                    print(linha)
                                time.sleep(3)

                                print("Conta encontrada. Operações de movimentação podem ser realizadas.")
                                print("-"*20)
                                print("MOVIMENTAÇÃO")
                                while True:
                                    print("1 - ADICIONAR ITEM AO CARRINHO")
                                    print("2 - CONFIRMAR COMPRA")
                                    print("3 - VOLTAR")
                                    mov_op = input("Escolha uma opção: ")

                                    if mov_op == '3':
                                        print("Retornando ao menu principal...")
                                        break

                                    elif mov_op == '1':
                                        codigo_produto = input("Digite o código do produto a ser adicionado ao carrinho: ")
                                        quantidade = int(input("Digite a quantidade a ser adicionada ao carrinho: "))
                                        with con.cursor() as cursor:
                                            cursor.execute("SELECT * FROM produtobeleza WHERE CODIGO = %s", (codigo_produto,))
                                            produto = cursor.fetchone()
                                            if produto:
                                                carrinho.append((codigo_produto, quantidade))
                                                print("Produto adicionado ao carrinho com sucesso!")
                                            else:
                                                print("Produto não encontrado.")

 

                                    elif mov_op == '2':
                                        print("RESUMO DO CARRINHO:")
                                        total = 0
                                        for item in carrinho:
                                            codigo_produto, quantidade = item
                                            with con.cursor() as cursor:
                                                cursor.execute("SELECT VALOR, ESTOQUE FROM produtobeleza WHERE CODIGO = %s", (codigo_produto,))
                                                produto_info = cursor.fetchone()
                                                if produto_info:
                                                    valor, estoque = produto_info
                                                    if estoque >= quantidade:
                                                        total += valor * quantidade
                                                    else:
                                                        print(f"Não há estoque suficiente para o produto de código {codigo_produto}.")
                                                        carrinho = []
                                                        break
                                                else:
                                                    print(f"Produto de código {codigo_produto} não encontrado no banco de dados.")
                                        else:
                                            print(f"Total a pagar: R${total:.2f}")
                                            confirmar = input("Deseja confirmar a compra? (S/N): ")
                                            if confirmar.upper() == 'S':
                                                for item in carrinho:
                                                    codigo_produto, quantidade = item
                                                    with con.cursor() as cursor:
                                                        cursor.execute("UPDATE produtobeleza SET ESTOQUE = ESTOQUE - %s WHERE CODIGO = %s", (quantidade, codigo_produto))
                                                        con.commit()
                                                print("Compra confirmada. Estoque atualizado.")
                                                carrinho = []                            
                                
                        else:
                            print("Conta não encontrada. Verifique o número da conta.")
    else:
        print("Opção inválida.")

    print("1 - CADASTRAR USER")
    print("2 - CADASTRAR PRODUTO")
    print("3 - MOVIMENTAR")
    print("4 - SAIR")
    op = input("Qual é a opção? ")

print("Até Breve...")


                       
