from Posicao import Posicao

class Campo:
    def __init__(self, id_jogador):
        self._id_jogador = id_jogador
        self.posicoes = [[Posicao(y, x, False) for x in range(5)] for y in range(3)]
        self.bases = []

    def campo_tem_base(self):
        for linha in self.posicoes:
            for posicao in linha:
                if posicao.get_defesa():
                    return True
        return False

    def remover_base_atingida(self, linha, coluna):
        if self.posicao_tem_base(linha, coluna):
            self.posicoes[linha][coluna].set_defesa(False)
            self.bases.remove((linha, coluna))

    def obter_posicoes_com_base(self):
        posicoes_com_base = []
        for y in range(3):
            for x in range(5):
                if self.posicoes[y][x].get_defesa():
                    posicoes_com_base.append((y, x))
        return posicoes_com_base

    def posicao_tem_base(self, linha, coluna):
        return self.posicoes[linha][coluna].get_defesa()

    def recupera_id_jogador(self):
        return self._id_jogador

    def pega_posicao(self, linha, coluna):
        return self.posicoes[linha][coluna]

    def pega_quantidade_bases(self):
        return len(self.bases)

    def adicionar_base(self, linha, coluna):
        if not self.posicao_tem_base(linha, coluna):
            self.posicoes[linha][coluna].set_defesa(True)
            self.bases.append((linha, coluna))
            print(f"Base adicionada na posição ({linha}, {coluna}) para o jogador {self._id_jogador}")
            print(f"Estado atual das bases: {self.obter_posicoes_com_base()}")

    def remover_base(self, linha, coluna):
        if self.posicao_tem_base(linha, coluna):
            self.posicoes[linha][coluna].set_defesa(False)
            self.bases.remove((linha, coluna))
            print(f"Base removida na posição ({linha}, {coluna}) para o jogador {self._id_jogador}")
            print(f"Estado atual das bases: {self.obter_posicoes_com_base()}")
