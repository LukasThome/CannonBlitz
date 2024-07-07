import random
from Tiro import Tiro

class TiroPreciso(Tiro):
    def __init__(self):
        super().__init__()

    def atirar(self, posicoes_com_base):
        # Obter as posições com base
        todas_as_posicoes = [(x, y) for x in range(3) for y in range(5)]
        
        # Filtrar posições sem bases
        lista_sorteadora = [pos for pos in todas_as_posicoes if pos not in posicoes_com_base]

        # Número de defesas é igual ao número de posições com bases
        num_defesas = len(posicoes_com_base)
        
        # Sortear posições
        posicoes_sorteadas = random.sample(lista_sorteadora, num_defesas)
        
        # Adicionar as posições com bases às posições sorteadas
        lista_sorteadora = posicoes_sorteadas + posicoes_com_base
        
        # Sortear uma posição da lista de sorteio
        posicao_sorteada = random.choice(lista_sorteadora)

        return posicao_sorteada
