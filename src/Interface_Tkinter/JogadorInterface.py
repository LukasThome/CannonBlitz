#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import messagebox , Menu, simpledialog
import random
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

from Dominio_do_problema import Tabuleiro
from Interface_Tkinter import Label
from Interface_Tkinter import Menu
from Interface_Tkinter import Frame
from Interface_Tkinter import TK
from DOG import StartStatus
from DOG import DogPlayerInterface

class JogadorInterface(DogPlayerInterface):

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

	def receber_desistencia(self):
		pass

	


class PlayerInterface(DogPlayerInterface):
    def __init__(self, master):
        self.master = master
        self.rows = 3
        self.cols = 5
        self.current_player = 1
        self.saldo = [0, 0]  # Saldo de cada jogador
        self.create_menu()  # Adicionando a criação do menu
        self.create_boards()
        self.create_controls()
        self.add_fixed_bases(self.board1)  # Adiciona bases fixas para o jogador
        self.add_fixed_bases(self.board2)  # Adiciona bases fixas para o oponente
        self.player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(self.player_name, self)
        messagebox.showinfo(message=message)


    def create_menu(self):
        # Criando o menu
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        # Adicionando opções ao menu
        self.game_menu = Menu(self.menu)
        self.menu.add_cascade(label="Menu", menu=self.game_menu)
        self.game_menu.add_command(label="Iniciar Partida", command=self.start_match)

    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        message = start_status.get_message()
        messagebox.showinfo(message=message)

    def receive_start(self, start_status):
        message = start_status.get_message()
        messagebox.showinfo(message=message)

    def create_boards(self):
        frame1 = tk.Frame(self.master)
        frame1.grid(row=0, column=0, padx=10, pady=10)
        self.board1 = []
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.cols):
                button = tk.Button(frame1, width=5, height=2, command=lambda row=i, col=j, player=1: self.button_click(row, col, player))
                button.grid(row=i, column=j, padx=1, pady=1)
                row_buttons.append(button)
            self.board1.append(row_buttons)

        tk.Label(self.master, text="").grid(row=1, column=0) #laber pra ter uma espaço em branco entre os dois grids

    
        frame2 = tk.Frame(self.master)
        frame2.grid(row=2, column=0, padx=3, pady=3)
        self.board2 = []
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.cols):
                button = tk.Button(frame2, width=5, height=2, command=lambda row=i, col=j, player=2: self.button_click(row, col, player))
                button.grid(row=i, column=j, padx=1, pady=1)
                row_buttons.append(button)
            self.board2.append(row_buttons)

    def add_fixed_bases(self, board):
        fixed_base_positions = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]  # Posições fixas das bases
        for row, col in fixed_base_positions:
            self.set_base_position(board[row][col])

    def create_controls(self):
        control_frame = tk.Frame(self.master)
        control_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

        self.saldo_label = tk.Label(control_frame, text=f"Saldo: {self.saldo[0]}")
        self.saldo_label.grid(row=0, column=0, padx=3, pady=3)

        self.comprar_base_button = tk.Button(control_frame, text="Comprar Base $2", command=self.comprar_base, state=tk.ACTIVE)
        self.comprar_base_button.grid(row=1, column=0, padx=3, pady=3)

        self.tiro_preciso_button = tk.Button(control_frame, text="Tiro Preciso $1", command=self.tiro_preciso, state=tk.ACTIVE)
        self.tiro_preciso_button.grid(row=2, column=0, padx=3, pady=3)

        self.base_button = tk.Button(control_frame, text="Tiro Normal", command=self.tiro_normal, state=tk.ACTIVE)
        self.base_button.grid(row=3, column=0, padx=3, pady=3)

        self.tiro_forte_button = tk.Button(control_frame, text="Tiro Forte $3", command=self.tiro_forte, state=tk.ACTIVE)
        self.tiro_forte_button.grid(row=4, column=0, padx=3, pady=3)


    def tiro_preciso(self):
        if self.saldo[self.current_player - 1] >= 1:
            # Deduz 1 do saldo do jogador atual
            self.saldo[self.current_player - 1] -= 1
            # Atualiza a exibição do saldo
            self.saldo_label.config(text=f"Saldo: {self.saldo[self.current_player - 1]}")
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)

            if self.board1[row][col]['bg'] == 'blue':  # Verifica se a posição do campo inimigo tem uma base
                self.saldo[0] += 1  # Adiciona 1 ao saldo do jogador 1
                self.saldo_label.config(text=f"Saldo: {self.saldo[0]}")  # Atualiza a exibição do saldo


            self.board1[row][col].configure(bg="red")
            self.master.after(2000, lambda: self.reset_board(row, col, self.board1))

           
            self.master.after(2000, self.computer_move)
        else:
            messagebox.showerror("Saldo Insuficiente", "Você não tem saldo suficiente para realizar um tiro preciso.")
        
    def tiro_normal(self):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.cols - 1)


        if self.board1[row][col]['bg'] == 'blue':  # Verifica se a posição do campo inimigo tem uma base
                self.saldo[0] += 1  # Adiciona 1 ao saldo do jogador 1
                self.saldo_label.config(text=f"Saldo: {self.saldo[0]}")  # Atualiza a exibição do saldo

        self.board1[row][col].configure(bg="red")
        self.master.after(2000, lambda: self.reset_board([(row, col)], self.board1))
        self.master.after(2000, self.computer_move)


    def tiro_forte(self):
        if self.saldo[self.current_player - 1] >= 3:
            # Deduz 3 do saldo do jogador atual
            self.saldo[self.current_player - 1] -= 3
            # Atualiza a exibição do saldo
            self.saldo_label.config(text=f"Saldo: {self.saldo[self.current_player - 1]}")

            start_row, start_col = random.randint(0, self.rows - 3), random.randint(0, self.cols - 3)
            affected_positions = []  # Lista para armazenar as posições afetadas pelo tiro forte

            # Atira forte em todas as posições
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    self.board1[i][j].configure(bg="red")
                    affected_positions.append((i, j))  # Adiciona a posição à lista de posições afetadas

            # Após um certo tempo, limpa apenas as posições afetadas pelo tiro forte
            self.master.after(2000, lambda: self.reset_board(affected_positions))

            self.master.after(2000, self.computer_move)
        else:
            messagebox.showerror("Saldo Insuficiente", "Você não tem saldo suficiente para realizar um tiro forte.")


    def comprar_base(self):
        if self.saldo[self.current_player - 1] >= 2:
            # Deduz 1 do saldo do jogador atual
            self.saldo[self.current_player - 1] -= 2
            # Atualiza a exibição do saldo
            self.saldo_label.config(text=f"Saldo: {self.saldo[self.current_player - 1]}")    

            for button_row in self.board2:
                for button in button_row:
                    button.config(command=lambda b=button: self.set_base_position(b))
            

        else:
            messagebox.showerror("Saldo Insuficiente", "Você não tem saldo suficiente para comprar uma base.")
        
        self.master.after(2000, self.computer_move)
    
    def highlight_random_position(self, color):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.cols - 1)
        self.board1[row][col].configure(bg=color)

    def set_base_position(self, button):
        button.config(bg="blue")
        button.config(command=lambda: None)  # Desativa a função de clique no botão
        
    def reset_board(self, positions, board):
        for row, col in positions:
            board[row][col].configure(bg="white")
        

    def computer_move(self):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.cols - 1)
        self.board2[row][col].configure(bg="red")
        self.master.after(2000, lambda: self.reset_board([(row, col)], self.board2))

        


   
def main():
    root = tk.Tk()
    root.title("Cannon Blitz")
    game = PlayerInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
