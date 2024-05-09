class Conta:
    def __init__(self, numero, saldo, ativo, cpf):
        self.numero = numero
        self.saldo = saldo
        self.ativo = ativo
        self.cpf = cpf
    
    def credito(self, valor):
        self.saldo += valor
    
    def debito(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Insira um valor coerente")

    def ativar(self):
        if not self.ativo:
            self.ativo = True
        else:
            print("Conta já está ativa")

    def mostrar(self):
        print( f"O seu saldo atual é {self.saldo}\n\n\n")
    


class Poupanca(Conta):
    def __init__(self, numero, saldo, ativo, cpf, aniversario):
        super().__init__(numero, saldo, ativo, cpf)
        self.aniversario = aniversario
    
    def atualizar_saldo(self, dia):
        if self.aniversario == dia:
            self.saldo += self.saldo * 0.05
        else:
            print("Ganhou nada KKKKKKKKKKKKKK")


class Corrente(Conta):
    def __init__(self, numero, saldo, ativo, cpf):
        super().__init__(numero, saldo, ativo, cpf)
    
    def pediTalao(self, cheques):
        if 0 < cheques <= 3:
            if self.saldo >= cheques * 30:
                self.saldo -= cheques * 30
            else: 
                print("Saldo insuficiente para emitir talão de cheques")
        else: 
            print("Número inválido de cheques")


class Especial(Conta):
    def __init__(self, numero, saldo, ativo, cpf):
        super().__init__(numero, saldo, ativo, cpf)
        self.limite = 1000
    
    def usarLimite(self):
        if self.saldo < 0:
            self.saldo += self.limite
            self.limite = 0
        elif self.limite == 0:
            print("Sem limite disponível")


class Empresa(Conta):
    def __init__(self, numero, saldo, ativo, cpf):
        super().__init__(numero, saldo, ativo, cpf)
        self.emprestimo = 10000
    
    def pedirEmprestimo(self, valor):
        if valor <= self.emprestimo:
            self.saldo -= valor
            self.emprestimo -= valor
        else:
            print("Valor de empréstimo excede o limite disponível")


class Estudantil(Conta):
    def __init__(self, numero, saldo, ativo, cpf):
        super().__init__(numero, saldo, ativo, cpf)
        self.emprestimo = 5000
    
    def pedirEmprestimo(self, valor):
        if valor <= self.emprestimo:
            self.saldo -= valor
            self.emprestimo -= valor
        else:
            print("Valor de empréstimo excede o limite disponível")



tipo = input("Escolha o tipo de conta (Poupança(P), Corrente(C), Especial(S), Empresa(M), Estudantil(E)): ")

# 
# 
# C1 = Empresa(0, 0, True, None, None)
# C1 = Estudantil(0, 0, True, None, None)
if tipo.lower() == "p":
        movimentos = 0
        niver = int(input("Qual é o seu aniversário?\n"))
        C1 = Poupanca(0, 0, True, None, niver)
        while movimentos <= 3:
            print("\n======= MENU =======")
            number = 0
            print("1. Débito")
            print("2. Crédito")
            op = int(input("Qual é a op?  "))
            if op == 1:
                if C1.saldo > 0:
                    valor = int(input("Valor?  "))
                    C1.debito(valor)
                    C1.mostrar()
                    movimentos +=1
                elif C1.saldo == 0:
                    print("Deposite primeiro, sem saldo")
                    C1.mostrar()

            elif op == 2:

                valor = int(input("Valor?  "))
                C1.credito(valor)
                C1.mostrar()
                movimentos +=1
                number +=1
            else:
                print("Coloca uma opcao decente bobao\n")
                C1.mostrar

        data = int(input("Qual é o dia de hoje?"))
        C1.atualizar_saldo(data)
        C1.mostrar()

                
                


elif tipo.lower() == "c":
        movimentos = 0
        C1 = Corrente(0, 0, True, None)

        while movimentos <= 3:
            print("\n======= MENU =======")
            number = 0
            print("1. Débito")
            print("2. Crédito")
            op = int(input("Qual é a op?  "))
            if op == 1:
                if C1.saldo > 0:
                    valor = int(input("Valor?  "))
                    C1.debito(valor)
                    C1.mostrar()
                    movimentos +=1
                elif C1.saldo == 0:
                    print("Deposite primeiro, sem saldo")
                    C1.mostrar()

            elif op == 2:

                valor = int(input("Valor?  "))
                C1.credito(valor)
                C1.mostrar()
                movimentos +=1
                number +=1
            else:
                print("Coloca uma opcao decente bobao\n")
                C1.mostrar
        
        op = input("Deseja cheques?(S/N)  ")
        if op.lower() == 's':
            
            qtd = int(input("Quantos precisas querido?  "))
            
            C1.pediTalao(qtd)
            C1.mostrar()
        else:
            print("bye")
        

elif tipo.lower() == "s":
    movimentos = 0
    C1 = Especial(0,0,True,None)

    while movimentos <= 3:
            print("\n======= MENU =======")
            number = 0
            print("1. Débito")
            print("2. Crédito")
            op = int(input("Qual é a op?  "))
            if op == 1:
                if C1.saldo > 0:
                    valor = int(input("Valor?  "))
                    C1.debito(valor)
                    C1.mostrar()
                    movimentos +=1
                elif C1.saldo == 0:
                    print("Deposite primeiro, sem saldo")
                    C1.mostrar()
                elif C1.saldo < 0:
                    C1.usarLimite()
                    movimentos +=1


            elif op == 2:

                valor = int(input("Valor?  "))
                C1.credito(valor)
                C1.mostrar()
                movimentos +=1
                number +=1
            else:
                print("Coloca uma opcao decente bobao\n")
                C1.mostrar()
    

        
# elif tipo.lower() == "m":
        
# elif tipo.lower() == "e":
        
# else:
#         print("Tipo de conta inválido!")


# moves = 0
# while moves < 10:
#         print("\n======= MENU =======")
#         print("1. Débito")
#         print("2. Crédito")
#         print("3. Usar Cheque")
#         print("4. Usar Empréstimo")
#         print("5. Usar Empréstimo Estudantil")
#         print("0. Sair")

#         op = input("Escolha uma opção: ")

#         if op == "1":
#             valor = float(input("Digite o valor para débito: "))
#             C1.debito(valor)
#         elif op == "2":
#             valor = float(input("Digite o valor para crédito: "))
#             C1.credito(valor)
#         elif op == "3":
#             C1.usar_cheque()
#         elif op == "4":
#             valor = float(input("Digite o valor para empréstimo: "))
#             C1.usar_empréstimo(valor)
#         elif op == "5":
#             valor = float(input("Digite o valor para empréstimo estudantil: "))
#             C1.usar_empréstimo_estudantil(valor)
#         elif op == "0":
#             print("Saindo...")
#             break
#         else:
#             print("Opção inválida.")

#         movimentos += 1
