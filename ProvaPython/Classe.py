class ProdutoBeleza:
    def __init__(self, codigo, descricao, marca, valor, estoque, id=0) -> None:
        self.id = id
        self.codigo = codigo
        self.descricao = descricao
        self.marca = marca
        self.valor = valor
        self.estoque = estoque


class Usuario:
    def __init__(self, email, senha, id = 0) -> None:
        self.id = id
        self.email = email
        self.senha = senha