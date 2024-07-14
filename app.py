from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

pastelMania = Restaurante('pastel mania', 'lanche')
picanhaMania = Restaurante('picanha mania', 'almoço')
suco = Bebida('Suco de Goiaba', 10, 'grande')
tapioca = Prato('Tapioca com Tucumã e Queijo', 15, 'Queijo coalho')
picanhaMania.adicionarItemCardapio(suco)
suco.aplicarDesconto()
picanhaMania.adicionarItemCardapio(tapioca)
tapioca.aplicarDesconto()

def main():

    picanhaMania.lisarCardapio
    pastelMania.lisarCardapio

if __name__ == '__main__':
    main()