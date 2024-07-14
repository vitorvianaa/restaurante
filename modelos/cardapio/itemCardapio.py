from abc import ABC, abstractmethod



class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco


    @abstractmethod # Siginifica que todas as classes filhos, vão herdar esse metodo, mas ele não é criado quando crio uma instancia da classe ItemCardapio 
    def aplicarDesconto(self):
        pass    