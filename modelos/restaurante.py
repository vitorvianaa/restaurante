from modelos.avaliacoes import Avaliacoes

class Restaurante:
    totalRestaurantes = [] 
    """
    Posso traduzir o self para 'ESTE'. Significa que estou dizendo para a função usar as variaveis daquela instancia em especifico
    ex: Como vou ter várias instancias da minha classe restaurante, o self siginifica que estou trabalhando variaveis daquela instancia em especifico
    """
    def __init__(self, nome, categoria):
        #Sel.nome = o nome dessa instancia
        self._nome = nome.title() # A primeira letra de cada palavra fica maiuscula
        #self.categoria = a categoria dessa instancia
        self._categoria = categoria.upper() # Tudo fica maiusculo
        self._status = False
        self.totalAvaliacoes = [] # Essa lista guarda objetos do tipo Avaliacoes
        Restaurante.totalRestaurantes.append(self)

    #qundo eu printo somente a instancia, ele me retorna o endereço de memoria que ela tá, e isso é irrelevante pra mim na maioria dos casos
    # Essa função diz que quando eu printar a instancia, ele vai me retornar o nome que foi atribuido a ela e nao o endereço de memoria
    def __str__(self):
        return self._nome

    
    @classmethod
    def listarRestaurantes(self):
        print('Listando Restaurantes:\n')
        for i, restaurente in enumerate(Restaurante.totalRestaurantes):
            print(f'ID: {i} || Nome: {restaurente._nome} || Categoria: {restaurente._categoria} || Avaliação: {restaurente.mediaAvaliacoes} ||Status: {restaurente.status}\n')

    
    def alterarStatus(self):
        self._status = not self._status
        print('Status alterado com sucesso!')

    def fazerAvaliacao(self, nomeCliente, nota):
        if nota < 0 or nota > 5:
            print('Não foi possivel fazer a avaliação.\nDigite um valor entre 0 e 5.')
        else:
            avaliacao = Avaliacoes(nomeCliente, nota)
            self.totalAvaliacoes.append(avaliacao)
            print('Avaliação feita com sucesso!')    
    
    @property
    def mediaAvaliacoes(self):
        # Verifica se a lista de av do obj tem alguma av
        if not self.totalAvaliacoes:
            return 'Sem Avaliações'
        else:
            totalNotas = sum(nota._nota for nota in self.totalAvaliacoes)
            totalAv = len(self.totalAvaliacoes)
            media = round(totalNotas / totalAv, 1)
            return media
        


    @property #Uso quando quero modificar a forma que o codigo lê um atributo especifico
    def status(self):
        return 'Ativo' if self._status else 'Inativo'



