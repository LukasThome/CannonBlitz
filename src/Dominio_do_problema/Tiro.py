#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class Tiro(object):
	__metaclass__ = ABCMeta
	@classmethod
	def atirar(self, aPosicoes_com_base):
		"""@ParamType aPosicoes_com_base <
		@ReturnType []"""
		pass

	@classmethod
	def __init__(self):
		self.___chance_acerto = None
		"""@AttributeType int"""
		self.___area_acerto = None
		"""@AttributeType int"""

