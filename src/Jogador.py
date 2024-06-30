
class Jogador:
    
	def __init__(self):
		self._nome = None
		self._vencedor = False
		self._turno = False
		self._saldo = 0
		self._id = None
		self._preencheu_bases = False
		
  		# self._unnamed_Tabuleiro_ = None
		# self._unnamed_Campo_ = None

	def definir_nome(self, nome):
		self._nome = nome

	def get_nome(self):
		return self._nome

	def definir_id(self, id):
		self._id = id


	def informar_turno(self):
		return self._turno

	def definir_jogador_vencedor(self):
		pass

	def aumentar_saldo_jogador(self, aSaldo):
		"""@ParamType aSaldo int"""
		pass

	def saldo_suficiente(self, aSaldo_necessario):
		return self._saldo >= aSaldo_necessario

	def diminuir_saldo(self, saldoDecremento):
		self. _saldo -= saldoDecremento

	def get_saldo(self):
		return self._saldo

	def set_turno(self, aTurno):
		self._turno = aTurno
		
	def set_vencedor(self):
		self._vencedor = True


	def definir_id(self, aId):
		"""@ParamType aId int"""
		pass



    