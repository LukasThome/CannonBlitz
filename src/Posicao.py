class Posicao:
    def __init__(self, linha, coluna, defesa):
        self.linha = linha
        self.coluna = coluna
        self.defesa = defesa

    def get_defesa(self):
        return self.defesa

    def set_defesa(self, defesa):
        self.defesa = defesa
