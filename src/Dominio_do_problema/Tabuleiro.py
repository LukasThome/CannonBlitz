#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Dominio_do_problema import Jogador
from Dominio_do_problema import Campo
from Dominio_do_problema import Canhao
from Interface_Tkinter import JogadorInterface
from Dominio_do_problema import ImagemInterface
from Dominio_do_problema import Posicao

class Tabuleiro(object):
	def tiro_normal(self):
		"""@ReturnType string"""
		pass

	def get_status_partida(self):
		"""@ReturnType int"""
		pass

	def comecar_partida(self, *aJogadores, aId_jogador_local, *aJogadores2, aId_jogador_local2):
		"""@ParamType aJogadores string*
		@ParamType aId_jogador_local string
		@ParamType aJogadores2 string*
		@ParamType aId_jogador_local2 string"""
		pass

	def set_status_partida(self, aStatus):
		"""@ParamType aStatus int
		@ReturnType int"""
		pass

	def ocupar_posicao(self, aLinha, aColuna):
		"""@ParamType aLinha int
		@ParamType aColuna int"""
		pass

	def diminuir_saldo_jogador(self, aSaldo):
		"""@ParamType aSaldo int"""
		pass

	def aumentar_saldo_jogador(self, aSaldo):
		"""@ParamType aSaldo int"""
		pass

	def verificar_saldo_jogador(self, aJogador):
		"""@ParamType aJogador Dominio do problema.Jogador"""
		pass

	def receber_jogada(self, aA_move):
		"""@ParamType aA_move Dictionary"""
		pass

	def verificar_bases_colocadas_pelo_jogador(self, *aBases):
		"""@ParamType aBases int*"""
		pass

	def verificar_base_comprada(self, aLinha, aColuna):
		"""@ParamType aLinha int
		@ParamType aColuna int"""
		pass

	def verificar_tiro_normal(self, aLinha, aColuna):
		"""@ParamType aLinha int
		@ParamType aColuna int"""
		pass

	def verificar_tiro_forte(self, aLinha, aColuna):
		"""@ParamType aLinha int
		@ParamType aColuna int"""
		pass

	def verificar_tiro_preciso(self, aLinha, aColuna):
		"""@ParamType aLinha int
		@ParamType aColuna int"""
		pass

	def verificar_jogada_vencedora(self, aCampo_jogador):
		"""@ParamType aCampo_jogador Dominio do problema.Campo
		@ReturnType boolean"""
		pass

	def definir_partida_finalizada(self):
		pass

	def gerar_item_jogada(self):
		"""@ReturnType Dictionary"""
		pass

	def verificar_partida_andamento(self):
		"""@ReturnType boolean"""
		pass

	def pega_campo_jogador_remoto(self):
		"""@ReturnType Dominio do problema.Campo"""
		pass

	def identificar_posicao_atingida(self, aCampo_jogador_remoto, aPosicao_atingida):
		"""@ParamType aCampo_jogador_remoto Dominio do problema.Campo
		@ParamType aPosicao_atingida Dominio do problema.Posicao
		@ReturnType boolean"""
		pass

	def calibrar_precisao_tiro_normal(self):
		pass

	def resetar_precisao_tiro_normal(self):
		pass

	def tiro_preciso(self):
		"""@ReturnType string"""
		pass

	def tiro_forte(self):
		"""@ReturnType string"""
		pass

	def verificar_numero_bases(self):
		"""@ReturnType Dominio do problema.Jogador"""
		pass

	def recupera_jogador_do_tiro_disparado_atraves_id_do_adversario(self, aId_jogador_dono_campo):
		"""@ParamType aId_jogador_dono_campo int
		@ReturnType Dominio do problema.Jogador"""
		pass

	def clicar_posicao_campo(self, aLinha, aColuna):
		"""@ParamType aLinha int
		@ParamType aColuna int
		@ReturnType string"""
		pass

	def sortear_turno(self):
		pass

	def comprar_base(self):
		pass

	def inicializar(self):
		pass

	def pegar_estado(self):
		"""@ReturnType Dominio do problema.Campo"""
		pass

	def receber_desistencia(self):
		pass

	def __init__(self):
		self._jogador_remoto = None
		"""@AttributeType Dominio do problema.Jogador"""
		self._jogador_local = None
		"""@AttributeType Dominio do problema.Jogador"""
		self._campo_jogador_local = None
		"""@AttributeType Dominio do problema.Campo"""
		self._status_partida = 1
		"""@AttributeType int"""
		self._campo_jogador_remoto = None
		"""@AttributeType Dominio do problema.Campo"""
		self._canhao_jogador_local = None
		"""@AttributeType Dominio do problema.Canhao"""
		self._canhao_jogador_remoto = None
		"""@AttributeType Dominio do problema.Canhao"""
		self._unnamed_JogadorInterface_ = None
		"""@AttributeType Interface Tkinter.JogadorInterface
		# @AssociationType Interface Tkinter.JogadorInterface"""
		self._unnamed_ImagemInterface_ = None
		"""@AttributeType Dominio do problema.ImagemInterface
		# @AssociationType Dominio do problema.ImagemInterface"""
		self._unnamed_Campo_ = []
		"""@AttributeType Dominio do problema.Campo*
		# @AssociationType Dominio do problema.Campo[]
		# @AssociationMultiplicity 2
		# @AssociationKind Composition"""
		self._unnamed_Jogador_ = []
		"""@AttributeType Dominio do problema.Jogador*
		# @AssociationType Dominio do problema.Jogador[]
		# @AssociationMultiplicity 2"""
		self._unnamed_Canhao_ = []
		"""@AttributeType Dominio do problema.Canhao*
		# @AssociationType Dominio do problema.Canhao[]
		# @AssociationMultiplicity 2
		# @AssociationKind Composition"""

