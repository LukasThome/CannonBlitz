import random
from Tiro import Tiro 

class TiroForte(Tiro):
    def __init__(self):
        super().__init__()
        self.area_acerto = 9

    def atirar(self, posicoes_campo):
        todas_as_posicoes = [(x, y) for x in range(3) for y in range(5)]
        campo = [pos for pos in todas_as_posicoes if pos not in posicoes_campo]

        # Escolhe uma posição central para o tiro forte
        posicao_central = random.choice(campo)

        # Define a área 3x3 ao redor da posição central
        posicoes_atingidas = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                pos = (posicao_central[0] + dx, posicao_central[1] + dy)
                if pos in todas_as_posicoes and pos not in posicoes_atingidas:
                    posicoes_atingidas.append(pos)

        self.area_acerto = len(posicoes_atingidas)
        return posicoes_atingidas
