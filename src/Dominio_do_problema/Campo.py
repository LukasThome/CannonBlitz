#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Dominio_do_problema import Tabuleiro
from Dominio_do_problema import Posicao
from Dominio_do_problema import Jogador

class Campo(object):
	def campo_tem_base(self):
		"""@ReturnType boolean"""
		pass

	def remover_base_atingida(self, aLinha, aColuna):
		"""@ParamType aLinha int
		@ParamType aColuna int
		@ReturnType void"""
		pass

	def obter_posicoes_com_base(self):
		"""@ReturnType <"""
		pass

	def posicao_tem_base(self, aLinha, aColuna):
		"""@ParamType aLinha int
		@ParamType aColuna int
		@ReturnType boolean"""
		pass

	def recupera_id_jogador(self):
		"""@ReturnType int"""
		pass

	def pega_posicao(self, aLinha, aColuna):
		"""@ParamType aLinha int
		@ParamType aColuna int
		@ReturnType Dominio do problema.Posicao"""
		pass

	def pega_quantidade_bases(self):
		"""@ReturnType int"""
		pass

	def __init__(self):
		self._posicoes = None
		"""@AttributeType posicao"""
		self._id_jogador = None
		"""@AttributeType int"""
		self._unnamed_Tabuleiro_ = None
		"""@AttributeType Dominio do problema.Tabuleiro
		# @AssociationType Dominio do problema.Tabuleiro"""
		self._unnamed_Posicao_ = []
		"""@AttributeType Dominio do problema.Posicao*
		# @AssociationType Dominio do problema.Posicao[]
		# @AssociationMultiplicity 15
		# @AssociationKind Composition"""
		self._unnamed_Jogador_ = None
		"""@AttributeType Dominio do problema.Jogador
		# @AssociationType Dominio do problema.Jogador
		# @AssociationMultiplicity 1"""

