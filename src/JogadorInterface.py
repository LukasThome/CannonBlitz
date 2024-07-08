from tkinter import *
from tkinter import messagebox, Menu, simpledialog
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from dog.start_status import StartStatus
from Tabuleiro import Tabuleiro
import threading

class JogadorInterface(DogPlayerInterface):

    def __init__(self):
        super().__init__()  # Chama o inicializador da classe pai, se necessário

        self.janela_principal = Tk()
        self.tabuleiro = Tabuleiro()
        self.desenhar_janela_principal()
        self.janela_principal.geometry("380x350")
        self.janela_principal.resizable(False, False)
        self.janela_principal.title("Cannon Blitz")

        player_name = simpledialog.askstring(title="Identificação do jogador", prompt="Qual o seu nome?")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)  # Mostra mensagem de conexão com o servidor

        self.janela_principal.mainloop()
        self.atualizar_interface()  # Atualiza a interface com o saldo inicial

    def desenhar_janela_principal(self):
        # Painel de Controle
        #Label(self.janela_principal, text="Cannon Blitz").grid(row=1, column=0)
        control_frame = Frame(self.janela_principal)
        control_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10)
        
        self.jogador_label = Label(control_frame, text=f"")
        self.jogador_label.grid(row=0, column=0, padx=3, pady=3)

        saldo_atual = self.tabuleiro.jogador_local.get_saldo()
        self.saldo_label = Label(control_frame, text=f"Saldo: {saldo_atual}")
        self.saldo_label.grid(row=1, column=0, padx=3, pady=3)

        self.comprar_base_button = Button(control_frame, text="Comprar Base $2", command=self.comprar_base, state=ACTIVE)
        self.comprar_base_button.grid(row=2, column=0, padx=3, pady=3)

        self.tiro_preciso_button = Button(control_frame, text="Tiro Preciso $1", command=self.tiro_preciso, state=ACTIVE)
        self.tiro_preciso_button.grid(row=3, column=0, padx=3, pady=3)

        self.base_button = Button(control_frame, text="Tiro Normal", command=self.tiro_normal, state=ACTIVE)
        self.base_button.grid(row=4, column=0, padx=3, pady=3)

        self.tiro_forte_button = Button(control_frame, text="Tiro Forte $3", command=self.tiro_forte, state=ACTIVE)
        self.tiro_forte_button.grid(row=5, column=0, padx=3, pady=3)

        # Menu
        self.menu = Menu(self.janela_principal)
        self.janela_principal.config(menu=self.menu)
        self.game_menu = Menu(self.menu)
        self.menu.add_cascade(label="Menu", menu=self.game_menu)
        self.game_menu.add_command(label="Iniciar Partida", command=self.iniciar_partida)

        # Campo jogador remoto (agora no topo)
        campo_jogador_remoto = Frame(self.janela_principal)
        campo_jogador_remoto.grid(row=0, column=0, padx=3, pady=3)
        self.board2 = []

        for i in range(3):
            row_buttons = []
            for j in range(5):
                button = Button(campo_jogador_remoto, width=5, height=2, state='disabled')
                button.grid(row=i, column=j, padx=1, pady=1)
                row_buttons.append(button)
            self.board2.append(row_buttons)

        # Campo jogador local (agora na parte inferior)
        campo_jogador_local = Frame(self.janela_principal)
        campo_jogador_local.grid(row=2, column=0, padx=10, pady=10)
        self.board1 = []

        for i in range(3):
            row_buttons = []
            for j in range(5):
                button = Button(campo_jogador_local, width=5, height=2, command=lambda i=i, j=j: self.clicar_posicao_campo(i, j))
                button.grid(row=i, column=j, padx=1, pady=1)
                row_buttons.append(button)
            self.board1.append(row_buttons)

        self.mensagem_label = Label(self.janela_principal, text="Aguardando início da partida", fg="red")
        self.mensagem_label.grid(row=3, column=0, padx=3, pady=3)

    def clicar_posicao_campo(self, linha, coluna):
        vez_jogador_local = self.tabuleiro.jogador_local.informar_turno()
        if vez_jogador_local:
            mensagem = self.tabuleiro.clicar_posicao_campo(linha,coluna)
            if mensagem != "Posição ocupada":
                self.atualizar_interface()
                status_partida = self.tabuleiro.get_estado()
                if status_partida == 2:
                    bases_jogador_local = self.tabuleiro.campo_jogador_local.pega_quantidade_bases()
                    if bases_jogador_local == 5:
                        self.tabuleiro.jogador_local.preencheu_bases = True
                        mensagem = "Você adicionou todas as suas bases. Aguarde o outro jogador."
                        move_to_send = {
                            'type': 'colocar_bases',
                            'positions': self.tabuleiro.campo_jogador_local.obter_posicoes_com_base(),
                            'match_status': 'next'  # Adicione esta linha para garantir a presença de 'match_status'
                        }
                        self.dog_server_interface.send_move(move_to_send)
                        if self.tabuleiro.jogador_remoto.preencheu_bases:
                            self.tabuleiro.set_estado(3)
                            if self.tabuleiro.jogador_local.informar_turno():
                                mensagem = "Partida em andamento. É a sua vez."
                            else:
                                mensagem = "Partida em andamento. Aguarde a vez do outro jogador."
                    else:
                        mensagem = "Continue até adicionar 5 bases"
                elif status_partida == 3 and mensagem == 'Base comprada adicionada! Aguarde o turno do outro jogador.':
                    self.comprar_base_button.config(state=ACTIVE)
                    self.tiro_preciso_button.config(state=ACTIVE)
                    self.base_button.config(state=ACTIVE)
                    self.tiro_forte_button.config(state=ACTIVE)
                    self.tabuleiro.set_comprando_base(False)
                    move_to_send = {
                        'type': 'comprar_base',
                        'linha': linha,
                        'coluna': coluna,
                        'match_status': 'next'
                    }
                    self.dog_server_interface.send_move(move_to_send)
        else:
            mensagem = "Não é seu turno"
        self.showinfo(mensagem)

    def iniciar_partida(self):
        if self.tabuleiro.estado == 1:
            status_inicio = self.dog_server_interface.start_match(2)  # Inicia a partida com 2 jogadores
            if status_inicio.get_code() == "2":
                jogadores = status_inicio.get_players()
                if len(jogadores) >= 2:
                    message = status_inicio.get_message()
                    if message == 'Partida iniciada':
                        self.showinfo("Partida iniciada, coloque suas bases")
                    else:
                        self.showinfo(message)
                    self.tabuleiro.comecar_partida(jogadores)
                    self.tabuleiro.set_estado(2)
                    self.jogador_label.config(text=f"Nome: {self.tabuleiro.get_nome_jogador_local()}")
                    self.atualizar_interface()
                else:
                    self.showinfo("Erro: jogadores insuficientes")
            else:
                self.showinfo("Erro ao iniciar partida: " + status_inicio.get_message())
        else:
            self.showinfo("Você já está em uma partida")

    def receive_start(self, start_status):
        jogadores = start_status.get_players()
        if len(jogadores) >= 2:
            self.tabuleiro.comecar_partida(jogadores)
            self.tabuleiro.set_estado(2)
            self.jogador_label.config(text=f"Nome: {self.tabuleiro.get_nome_jogador_local()}")
            message = start_status.get_message()
            if message == 'Partida iniciada':
                self.showinfo("Partida iniciada, coloque suas bases")
            else:
                self.showinfo(message)
            self.atualizar_interface()
        else:
            self.showinfo("Erro: jogadores insuficientes")

    def receive_move(self, a_move):
            mensagem = self.tabuleiro.receber_jogada(a_move)
            if mensagem is not None:
                self.showinfo(mensagem)
            else:     
                if self.tabuleiro.jogador_local.informar_turno():
                    self.showinfo("Partida em andamento. É a sua vez.")
                else:
                    self.showinfo("Partida em andamento. Aguarde a vez do outro jogador.")
            move_type = a_move.get('type')
            if move_type == 'tiro_normal' or move_type == 'tiro_preciso':
                return self.atualizar_interface([(a_move.get('linha'), a_move.get('coluna'))])
            elif move_type == 'tiro_forte':
                return self.atualizar_interface([tuple(pos) for pos in a_move.get('posicoes_atingidas')])
            else:
                self.atualizar_interface()
            
    def comprar_base(self):
        mensagem = self.tabuleiro.comprar_base()
        if mensagem == 'Clique na posição desejada para colocar a base':
            self.comprar_base_button.config(state=DISABLED)
            self.tiro_preciso_button.config(state=DISABLED)
            self.base_button.config(state=DISABLED)
            self.tiro_forte_button.config(state=DISABLED)
            self.tabuleiro.set_comprando_base(True)
        self.showinfo(mensagem)
        self.atualizar_interface()

    def tiro_normal(self):
        mensagem,linha,coluna = self.tabuleiro.tiro_normal()
        self.showinfo(mensagem)
        self.atualizar_interface([(linha, coluna)])

        if mensagem != 'Não é seu turno' and mensagem != "A partida deve estar em andamento! Inicie uma partida no menu principal":
            move_to_send = {
                'type': 'tiro_normal',
                'linha': linha,
                'coluna': coluna,
                'match_status': 'next'
            }
            self.dog_server_interface.send_move(move_to_send)
            
    def tiro_preciso(self):
        mensagem,linha,coluna = self.tabuleiro.tiro_preciso()
        self.showinfo(mensagem)
        self.atualizar_interface([(linha, coluna)])

        if mensagem != "A partida deve estar em andamento! Inicie uma partida no menu principal" and mensagem != 'Não é seu turno' and mensagem != 'Saldo insuficiente':
            move_to_send = {
                'type': 'tiro_preciso',
                'linha': linha,
                'coluna': coluna,
                'match_status': 'next'
            }
            self.dog_server_interface.send_move(move_to_send)

    def tiro_forte(self):
        mensagem, posicoes_atingidas = self.tabuleiro.tiro_forte()
        self.showinfo(mensagem)
        self.atualizar_interface(posicoes_atingidas)
        if mensagem != "A partida deve estar em andamento! Inicie uma partida no menu principal! Inicie uma partida no menu principal" and mensagem != 'Não é seu turno' and mensagem != 'Saldo insuficiente':
            move_to_send = {
                'type': 'tiro_forte',
                'posicoes_atingidas': posicoes_atingidas,
                'match_status': 'next'
            }
            self.dog_server_interface.send_move(move_to_send)

    def atualizar_interface(self, posicoes_atingidas=None):
        self.saldo_label.config(text=f"Saldo: {self.tabuleiro.jogador_local.get_saldo()}")
        # Atualize a visualização do tabuleiro com as bases do jogador local e remoto
        for y in range(3):
            for x in range(5):
                if posicoes_atingidas is not None and (y, x) in posicoes_atingidas:
                    if self.tabuleiro.jogador_local.informar_turno():
                        self.board1[y][x].configure(bg='yellow')
                    else:
                        self.board2[y][x].configure(bg='yellow')
                else:
                    if self.tabuleiro.campo_jogador_local.posicao_tem_base(y, x):
                        self.board1[y][x].configure(bg='green')
                    else:
                        self.board1[y][x].configure(bg='white')

                    if self.tabuleiro.campo_jogador_remoto.posicao_tem_base(y, x):
                        self.board2[y][x].configure(bg='red')
                    else:
                        self.board2[y][x].configure(bg='white')

        # Se um tiro foi efetuado, agenda a limpeza dos campos acertados após 2 segundos
        if posicoes_atingidas is not None:
            temporizador = threading.Timer(2.0, lambda: self.limpar_sinalizador_de_tiro_da_rodada(posicoes_atingidas))
            temporizador.start()

    def limpar_sinalizador_de_tiro_da_rodada(self, posicoes_atingidas):
        for y, x in posicoes_atingidas:
            if y is not None and x is not None:
                if self.tabuleiro.jogador_local.informar_turno():
                    self.board1[y][x].configure(bg='white')
                else:
                    self.board2[y][x].configure(bg='white')

    #adicionar no diagrama
    def sincronizar_turno(self, turnos):
        if self.tabuleiro.jogador_local.id == turnos.get('jogador_local_id'):
            self.tabuleiro.jogador_local.set_turno(turnos.get('jogador_local_turno', False))
            self.tabuleiro.jogador_remoto.set_turno(turnos.get('jogador_remoto_turno', False))
        else:
            self.tabuleiro.jogador_local.set_turno(turnos.get('jogador_remoto_turno', False))
            self.tabuleiro.jogador_remoto.set_turno(turnos.get('jogador_local_turno', False))

        self.atualizar_interface()

    def receive_withdrawal_notification(self):
        self.tabuleiro.receber_desistencia()
        self.showinfo("Seu oponente desistiu!")
        self.atualizar_interface()
        
    def showinfo(self, mensagem):
        self.mensagem_label.config(text=mensagem)