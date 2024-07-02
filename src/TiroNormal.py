import random
from  Tiro import Tiro

class TiroNormal(Tiro):
    def __init__(self):
        super().__init__()
        self.precisao = 0

    def resetar_precisao(self):
        self.precisao = 0

    def calibrar_precisao(self):
        self.precisao += 1

    def atirar(self, posicoes_com_base):
        todas_as_posicoes = [(x, y) for x in range(3) for y in range(5)]
        posicoes_livres = [pos for pos in todas_as_posicoes if pos not in posicoes_com_base]

        # Remove N posições da lista de posições livres, onde N = precisao
        posicoes_removidas = random.sample(posicoes_livres, min(self.precisao, len(posicoes_livres)))
        for pos in posicoes_removidas:
            posicoes_livres.remove(pos)

        # Adiciona as posições com base de volta à lista
        posicoes_livres.extend(posicoes_com_base)

        # Seleciona uma posição aleatória da lista
        posicao_sorteda = random.choice(posicoes_livres)
        print(f"Posição do tiro: {posicao_sorteda}")
        return posicao_sorteda
