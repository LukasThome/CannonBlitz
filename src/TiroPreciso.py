import random
from Tiro import Tiro

class TiroPreciso(Tiro):
    def __init__(self):
        super().__init__()

    def atirar(self, posicoes_com_base):
        todas_as_posicoes = [(x, y) for x in range(3) for y in range(5)]
        posicoes_livres = [pos for pos in todas_as_posicoes if pos not in posicoes_com_base]

        # 50% de chance de tentar acertar uma posição com base
        if random.choice([True, False]) and posicoes_com_base:
            posicao_sorteda = random.choice(posicoes_com_base)
        else:
            # Se não houver bases ou se a chance não for selecionada, escolhe uma posição livre
            posicao_sorteda = random.choice(posicoes_livres) if posicoes_livres else None
        return posicao_sorteda
