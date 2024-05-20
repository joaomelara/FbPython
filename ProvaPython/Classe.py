class ProdutoBeleza:
    def __init__(self, codigo, descricao, marca, valor, estoque, id=0):
        self.id = id
        self.codigo = codigo
        self.descricao = descricao
        self.marca = marca
        self.valor = valor
        self.estoque = estoque

    def adicionar_estoque(self, quantidade):
        if 0 < quantidade <= 30:
            self.estoque = quantidade
            return True
        return False

    def remover_estoque(self, quantidade):
        if 0 <= quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        return False





class Usuario:
    def __init__(self, email, senha, id = 0):
        self.id = id
        self.email = email
        self.senha = senha