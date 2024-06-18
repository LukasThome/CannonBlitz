#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Dominio_do_problema import Tabuleiro
from Interface_Tkinter import Label
from Interface_Tkinter import Menu
from Interface_Tkinter import Frame
from Interface_Tkinter import TK
from DOG import StartStatus
from DOG import DogPlayerInterface

class JogadorInterface(DogPlayerInterface):
	def atualizar_interface(self):
		pass

	def desenhar_janela_principal(self):
		pass

	def tiro_normal(self):
		pass

	def receber_inicio(self, aStatus_inicio):
		"""@ParamType aStatus_inicio DOG.StartStatus"""
		pass

	def iniciar_partida(self):
		pass

	def receive_start(self, aStart_status):
		"""@ParamType aStart_status DOG.StartStatus"""
		pass

	def receive_move(self, aA_move):
		"""@ParamType aA_move Dictionary"""
		pass

	def receive_withdrawal_notification(self):
		pass

	def request_player_name(self):
		"""@ReturnType string"""
		pass

	def notify_result(self, aMessage):
		"""@ParamType aMessage string"""
		pass

	def proceed_start(self, *aPlayers, aLocal_player_id):
		"""@ParamType aPlayers string*
		@ParamType aLocal_player_id string"""
		pass

	def atualizar_interface(self, aStatus):
		"""@ParamType aStatus Dominio do Problema.ImagemInterface"""
		pass

	def operation(self):
		pass

	def pegar_posicao_campo(self, aLinha, aColuna):
		"""@ParamType aLinha int
		@ParamType aColuna int"""
		pass

	def comecar_partida(self):
		pass

	def tiro_preciso(self):
		pass

	def tiro_forte(self):
		pass

	def comprar_base(self):
		pass

	def colocar_bases(self):
		pass

	def clicar_posicao_campo(self, aLinha, aColuna):
		"""@ParamType aLinha int
		@ParamType aColuna int"""
		pass

	def __init__(self):
		self._janela_principal = None
		"""@AttributeType Tk"""
		self._tabuleiro = None
		"""@AttributeType Dominio do problema.Tabuleiro"""
		self._logo_label = None
		"""@AttributeType Interface Tkinter.Label"""
		self._nome_jogador = None
		"""@AttributeType string"""
		self._dog_server_interface_DogActor = None
		self._mensagem = None
		"""@AttributeType Interface Tkinter.Label"""
		self._barra_menu = None
		"""@AttributeType Interface Tkinter.Menu"""
		self._arquivo_menu = None
		"""@AttributeType Interface Tkinter.Menu"""
		self._frame = None
		"""@AttributeType Interface Tkinter.Frame"""
		self._unnamed_Frame_ = None
		"""@AttributeType Interface Tkinter.Frame
		# @AssociationType Interface Tkinter.Frame
		# @AssociationMultiplicity 1
		# @AssociationKind Aggregation"""
		self._unnamed_Menu_ = []
		"""@AttributeType Interface Tkinter.Menu*
		# @AssociationType Interface Tkinter.Menu[]
		# @AssociationMultiplicity 2
		# @AssociationKind Aggregation"""
		self._unnamed_Label_ = []
		"""@AttributeType Interface Tkinter.Label*
		# @AssociationType Interface Tkinter.Label[]
		# @AssociationMultiplicity 2
		# @AssociationKind Aggregation"""
		self._unnamed_TK_ = None
		"""@AttributeType Interface Tkinter.TK
		# @AssociationType Interface Tkinter.TK
		# @AssociationMultiplicity 1
		# @AssociationKind Aggregation"""
		self._unnamed_Tabuleiro_ = None
		"""@AttributeType Dominio do problema.Tabuleiro
		# @AssociationType Dominio do problema.Tabuleiro"""

	def receber_desistencia(self):
		pass

