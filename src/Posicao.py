

class Posicao:
	def __init__(self,linha,coluna,defesa):
		self.defesa = defesa
		self.linha = linha
		self.coluna = coluna

	def get_defesa(self):
		return self._defesa

	def set_defesa(self, defesa):
		self.defesa= defesa
