
class Jogador:
    
	def __init__(self):
		self.nome = None
		self.vencedor = False
		self.turno = False
		self.saldo = 0
		self.id = None
		self.preencheu_bases = False
		
  		# self._unnamed_Tabuleiro_ = None
		# self._unnamed_Campo_ = None

	def definir_nome(self, nome):
		self.nome = nome

	# def get_nome(self):
	# 	return self._nome

	def definir_id(self, id):
		self.id = id

	def informar_turno(self):
		return self.turno

	def definir_jogador_vencedor(self):
		self.vencedor = True
	
	def aumentar_saldo_jogador(self, saldoAcrescimo):
		self.saldo += saldoAcrescimo

	def saldo_suficiente(self, aSaldo_necessario):
		return self.saldo >= aSaldo_necessario

	def diminuir_saldo(self, saldoDecremento):
		self.saldo -= saldoDecremento

	def get_saldo(self):
		return self.saldo

	def set_turno(self, aTurno):
		self.turno = aTurno
		
	def set_vencedor(self):
		self.vencedor = True
   