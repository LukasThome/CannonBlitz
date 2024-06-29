# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from Dominio_do_problema import Canhao
# from Dominio_do_problema import Tiro

# class TiroForte(Tiro):
# 	def __init__(self):
# 		self._unnamed_Canhao_ = None
# 		"""@AttributeType Dominio do problema.Canhao
# 		# @AssociationType Dominio do problema.Canhao"""

# Importa a classe Tiro corretamente
from Tiro import Tiro

class TiroForte(Tiro):
    def __init__(self):
        super().__init__()
        # Inicialização adicional para TiroForte
        pass