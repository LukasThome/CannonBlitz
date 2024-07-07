import random
from Tiro import Tiro

class TiroPreciso(Tiro):
    def __init__(self):
        super().__init__()
        self.precisao = 0

    def atirar(self, posicoes_com_base):
        todas_as_posicoes = [(x, y) for x in range(3) for y in range(5)]
        posicoes_livres = [pos for pos in todas_as_posicoes if pos not in posicoes_com_base]

        # Remove posições livres de acordo com a precisão
        posicoes_removidas = random.sample(posicoes_livres, min(self.precisao, len(posicoes_livres)))
        for pos in posicoes_removidas:
            posicoes_livres.remove(pos)

        # 50% de chance de tentar acertar uma base com defesa
        if random.choice([True, False]) and posicoes_com_base:
            posicao_sorteda = random.choice(posicoes_com_base)
        else:
            # Se não houver bases com defesa ou se a chance não for selecionada, escolhe uma posição livre
            posicao_sorteda = random.choice(posicoes_livres) if posicoes_livres else None
        
        print(f"Posição do tiro: {posicao_sorteda}")
        return posicao_sorteda