#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Dominio_do_problema import Campo

class Posicao(object):
	def get_defesa(self):
		"""@ReturnType boolean"""
		pass

	def set_defesa(self, aDefesa):
		"""@ParamType aDefesa boolean
		@ReturnType void"""
		pass

	def __init__(self):
		self._defesa = None
		"""@AttributeType boolean"""
		self._linha = None
		"""@AttributeType int"""
		self._coluna = None
		"""@AttributeType int"""
		self._unnamed_Campo_ = None
		"""@AttributeType Dominio do problema.Campo
		# @AssociationType Dominio do problema.Campo"""
