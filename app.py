from modelos.restaurante import Restaurante


picanhaMania = Restaurante('picanha mania', 'almoço')
pastelMania = Restaurante('pastel mania', 'lanche')
bobs = Restaurante('Bobs', 'fastfood')
bobs.alterarStatus()

pastelMania.fazerAvaliacao('Vitor', 4)
pastelMania.fazerAvaliacao('Maria', 5)

def main():

    Restaurante.listarRestaurantes()

if __name__ == '__main__':
    main()