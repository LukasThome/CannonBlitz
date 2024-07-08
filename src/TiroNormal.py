import random
from Tiro import Tiro

class TiroNormal(Tiro):
    def __init__(self):
        super().__init__()
        self.precisao = 0

    def resetar_precisao(self):
        self.precisao = 0

    def calibrar_precisao(self):
        self.precisao += 1

    def atirar(self, posicoes_com_base):
        # Gerar todas as posições possíveis (3x5)
        todas_as_posicoes = [(x, y) for x in range(3) for y in range(5)]
        
        # Filtrar posições sem bases
        lista_sorteadora = [pos for pos in todas_as_posicoes if pos not in posicoes_com_base]
        
        # Remover posições de acordo com a precisão
        posicoes_removidas = random.sample(lista_sorteadora, min(self.precisao, len(lista_sorteadora)))
        for pos in posicoes_removidas:
            lista_sorteadora.remove(pos)
        
        # Adicionar as posições com bases às posições sorteadas
        lista_sorteadora.extend(posicoes_com_base)
        
        # Sortear uma posição da lista de sorteio
        posicao_sorteda = random.choice(lista_sorteadora)

        return posicao_sorteda
