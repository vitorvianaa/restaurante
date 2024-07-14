from modelos.cardapio.itemCardapio import ItemCardapio

# passo com parametro a minha classe 'pai' e a classe 'filho' herda metodos, atributos da classe pai
# Prato herda ItemCardapio 
class Prato(ItemCardapio):
    # Uso os atribuutos nome e preco da classe pai e defino a descricao, que é um atributo especifico da classe prato
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicarDesconto(self):
        self._preco -= (self._preco * 0.08)