#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Dominio_do_problema import Canhao
from Dominio_do_problema import Tiro

class TiroNormal(Tiro):
	def resetar_precisao(self):
		pass

	def calibrar_precisao(self):
		pass

	def __init__(self):
		self._precisao = None
		"""@AttributeType int"""
		self._unnamed_Canhao_ = None
		"""@AttributeType Dominio do problema.Canhao
		# @AssociationType Dominio do problema.Canhao"""

