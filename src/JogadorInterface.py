from tkinter import *
from tkinter import messagebox, Menu, simpledialog
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from Tabuleiro import Tabuleiro  # Importa a classe Tabuleiro do arquivo Tabuleiro.py


class JogadorInterface(DogPlayerInterface):

    def __init__(self):    
        self.janela_principal = Tk()
        self.desenhar_janela_principal()
        self.tabuleiro = Tabuleiro()  
        nome_jogador = simpledialog.askstring(title="Identificador do Jogador", prompt="Qual o seu nome?")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(nome_jogador, self)
        messagebox.showinfo(message=message)
         # self.barra_menu = Menu()
        # self.arquivo_menu = Menu()
    
    def atualizar_interface(self):
        pass

    def desenhar_janela_principal(self):
        # Tabuleiros
        frame1 = Frame(self.janela_principal)
        frame1.grid(row=0, column=0, padx=10, pady=10)
        self.board1 = []
        
        for i in range(3):
            row_buttons = []
            for j in range(5):
                button = Button(frame1, width=5, height=2, command=lambda row=i, col=j, player=1: self.button_click(row, col, player))
                button.grid(row=i, column=j, padx=1, pady=1)
                row_buttons.append(button)
            self.board1.append(row_buttons)

        Label(self.janela_principal, text="").grid(row=1, column=0)

        # Botões
        control_frame = Frame(self.janela_principal)
        control_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

        self.saldo_label = Label(control_frame, text="Saldo: 0")
        self.saldo_label.grid(row=0, column=0, padx=3, pady=3)

        self.comprar_base_button = Button(control_frame, text="Comprar Base $2", command=self.comprar_base, state=ACTIVE)
        self.comprar_base_button.grid(row=1, column=0, padx=3, pady=3)

        self.tiro_preciso_button = Button(control_frame, text="Tiro Preciso $1", command=self.tiro_preciso, state=ACTIVE)
        self.tiro_preciso_button.grid(row=2, column=0, padx=3, pady=3)

        self.base_button = Button(control_frame, text="Tiro Normal", command=self.tiro_normal, state=ACTIVE)
        self.base_button.grid(row=3, column=0, padx=3, pady=3)

        self.tiro_forte_button = Button(control_frame, text="Tiro Forte $3", command=self.tiro_forte, state=ACTIVE)
        self.tiro_forte_button.grid(row=4, column=0, padx=3, pady=3)
        
        # Menu
        self.menu = Menu(self.janela_principal)
        self.janela_principal.config(menu=self.menu)

        self.game_menu = Menu(self.menu)
        self.menu.add_cascade(label="Menu", menu=self.game_menu)
        self.game_menu.add_command(label="Iniciar Partida", command=self.iniciar_partida)
   
    def button_click(self, row, col, player):
        # Placeholder function for button clicks
        pass

    def tiro_normal(self):
        pass

    def receber_inicio(self, aStatus_inicio):
        pass

    def iniciar_partida(self):
        pass

    def receive_start(self, aStart_status):
        pass

    def receive_move(self, aA_move):
        pass

    def receive_withdrawal_notification(self):
        pass

    def request_player_name(self):
        pass

    def notify_result(self, aMessage):
        pass

    def proceed_start(self, *aPlayers, aLocal_player_id):
        pass

    def atualizar_interface(self, aStatus):
        pass

    def operation(self):
        pass

    def pegar_posicao_campo(self, aLinha, aColuna):
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
        pass

    def receber_desistencia(self):
        pass

if __name__ == "__main__":
    JogadorInterface()
    mainloop()
