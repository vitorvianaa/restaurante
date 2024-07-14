from modelos.cardapio.itemCardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome
    
    def aplicarDesconto(self):
        self._preco -= (self._preco * 0.05)