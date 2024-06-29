from Campo import Campo 

class Jogador:
    
	def informar_turno(self):
		"""@ReturnType boolean"""
		pass

	def definir_jogador_vencedor(self):
		pass

	def aumentar_saldo_jogador(self, aSaldo):
		"""@ParamType aSaldo int"""
		pass

	def saldo_suficiente(self, aSaldo_necessario):
		"""@ParamType aSaldo_necessario int
		@ReturnType boolean"""
		pass

	def diminuir_saldo(self, aSaldo):
		"""@ParamType aSaldo int"""
		pass

	def get_saldo(self):
		"""@ReturnType int"""
		pass

	def set_turno(self):
		"""@ReturnType boolean"""
		pass

	def set_vencedor(self):
		"""@ReturnType boolean"""
		pass

	def definir_nome(self, aNome):
		"""@ParamType aNome string"""
		pass

	def definir_id(self, aId):
		"""@ParamType aId int"""
		pass

	def __init__(self):
		self._nome = None
		"""@AttributeType string"""
		self._vencedor = False
		"""@AttributeType boolean"""
		self._turno = False
		"""@AttributeType boolean"""
		self._saldo = 0
		"""@AttributeType int"""
		self._id = None
		"""@AttributeType int"""
		self._preencheu_bases = False
		"""@AttributeType boolean"""
		self._unnamed_Tabuleiro_ = None
		"""@AttributeType Dominio do problema.Tabuleiro
		# @AssociationType Dominio do problema.Tabuleiro"""
		self._unnamed_Campo_ = None
		"""@AttributeType Dominio do problema.Campo
		# @AssociationType Dominio do problema.Campo
		# @AssociationMultiplicity 1"""

