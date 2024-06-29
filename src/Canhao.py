# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Dominio_do_problema import TiroNormal
# from Dominio_do_problema import TiroForte
# from Dominio_do_problema import TiroPreciso
# from Dominio_do_problema import Jogador
# from Dominio_do_problema import Tabuleiro
# from Dominio_do_problema import Campo

# #class Canhao(object):
# class Canhao():
    
# 	def resetar_precisao_tiro_normal(self):
# 		pass

# 	def calibrar_precisao(self):
# 		pass

# 	def tiro_normal(self, aCampo_jogador_remoto):
# 		"""@ParamType aCampo_jogador_remoto Dominio do problema.Campo"""
# 		pass

# 	def tiro_preciso(self, aCampo_jogador_remoto):
# 		"""@ParamType aCampo_jogador_remoto Dominio do problema.Campo"""
# 		pass

# 	def tiro_forte(self, aCampo_jogador_remoto):
# 		"""@ParamType aCampo_jogador_remoto Dominio do problema.Campo"""
# 		pass

# 	def __init__(self):
# 		self._tiro_normal = None
# 		"""@AttributeType Dominio do problema.TiroNormal"""
# 		self._tiro_forte = None
# 		"""@AttributeType Dominio do problema.TiroForte"""
# 		self._tiro_preciso = None
# 		"""@AttributeType Dominio do problema.TiroPreciso"""
# 		self._jogador = None
# 		"""@AttributeType Dominio do problema.Jogador"""
# 		self._id_jogador = None
# 		"""@AttributeType int"""
# 		self._unnamed_TiroNormal_ = None
# 		"""@AttributeType Dominio do problema.TiroNormal
# 		# @AssociationType Dominio do problema.TiroNormal
# 		# @AssociationMultiplicity 1"""
# 		self._unnamed_Tabuleiro_ = None
# 		"""@AttributeType Dominio do problema.Tabuleiro
# 		# @AssociationType Dominio do problema.Tabuleiro"""
# 		self._unnamed_TiroForte_ = None
# 		"""@AttributeType Dominio do problema.TiroForte
# 		# @AssociationType Dominio do problema.TiroForte
# 		# @AssociationMultiplicity 1"""
# 		self._unnamed_TiroPreciso_ = None
# 		"""@AttributeType Dominio do problema.TiroPreciso
# 		# @AssociationType Dominio do problema.TiroPreciso
# 		# @AssociationMultiplicity 1"""



from TiroForte import TiroForte

class Canhao:
    def __init__(self):
        # Inicialização da classe Canhao
        self.tiro_forte = TiroForte()