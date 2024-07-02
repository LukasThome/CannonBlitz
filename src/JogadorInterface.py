from tkinter import *
from tkinter import messagebox, Menu, simpledialog
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from dog.start_status import StartStatus
from Tabuleiro import Tabuleiro

class JogadorInterface(DogPlayerInterface):

    def __init__(self):
        super().__init__()  # Chama o inicializador da classe pai, se necessário

        self.janela_principal = Tk()
        self.tabuleiro = Tabuleiro()
        self.desenhar_janela_principal()

        player_name = simpledialog.askstring(title="Identificação do jogador", prompt="Qual o seu nome?")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)  # Mostra mensagem de conexão com o servidor

        self.janela_principal.mainloop()
        self.atualizar_interface()  # Atualiza a interface com o saldo inicial

    def desenhar_janela_principal(self):
        # Painel de Controle
        Label(self.janela_principal, text="Cannon Blitz").grid(row=1, column=0)
        control_frame = Frame(self.janela_principal)
        control_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

        saldo_atual = self.tabuleiro.jogador_local.get_saldo()
        self.saldo_label = Label(control_frame, text=f"Saldo: {saldo_atual}")
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

        # Campo jogador remoto (agora no topo)
        campo_jogador_remoto = Frame(self.janela_principal)
        campo_jogador_remoto.grid(row=0, column=0, padx=3, pady=3)
        self.board2 = []

        for i in range(3):
            row_buttons = []
            for j in range(5):
                button = Button(campo_jogador_remoto, width=5, height=2, command=lambda i=i, j=j: self.clicar_posicao_campo(i, j))
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
                button.configure(bg='green')  # Define o fundo do botão como verde
                row_buttons.append(button)
            self.board1.append(row_buttons)

        self.mensagem_label = Label(self.janela_principal, text="", fg="red")
        self.mensagem_label.grid(row=3, column=0, padx=3, pady=3)

    def clicar_posicao_campo(self, linha, coluna):
        print(f"Clique registrado na linha {linha}, coluna {coluna}")

        estado_partida = self.tabuleiro.get_estado()

        if estado_partida not in [2, 3]:
            self.mensagem_label.config(text="Aguardando início da partida")
            return

        if not self.tabuleiro.jogador_local.informar_turno():
            self.mensagem_label.config(text="Não é seu turno")
            return

        if self.tabuleiro.campo_jogador_local.posicao_tem_base(linha, coluna):
            self.mensagem_label.config(text="Posição ocupada")
            print(f"A posição ({linha}, {coluna}) já está ocupada.")
            return

        self.tabuleiro.campo_jogador_local.adicionar_base(linha, coluna)
        print(f"Base adicionada na posição ({linha}, {coluna}) pelo jogador local")
        print(f"Bases ocupadas: {self.tabuleiro.campo_jogador_local.obter_posicoes_com_base()}")
        print(f"Quantidade de bases: {self.tabuleiro.campo_jogador_local.pega_quantidade_bases()}")
        print(f"Informações do jogador local: {vars(self.tabuleiro.jogador_local)}")
        print(f"Informações do jogador remoto: {vars(self.tabuleiro.jogador_remoto)}")
        print(f"Estado da partida: {self.tabuleiro.get_estado()}")
        self.atualizar_interface()

        if estado_partida == 2:
            if self.tabuleiro.campo_jogador_local.pega_quantidade_bases() == 5:
                self.tabuleiro.jogador_local.preencheu_bases = True
                if self.tabuleiro.jogador_local.preencheu_bases and self.tabuleiro.jogador_remoto.preencheu_bases:
                    self.tabuleiro.set_estado(3)
                    self.mensagem_label.config(text="Estado da partida atualizado para 'em andamento'")
                else:
                    self.mensagem_label.config(text="Você adicionou todas as suas bases. Aguarde o outro jogador.")
            else:
                self.mensagem_label.config(text="Continue até adicionar 5 bases")
        elif estado_partida == 3:
            # Enviar jogada para o DOG (adapte conforme necessário)
            move_to_send = self.tabuleiro.gerar_item_jogada()
            self.dog_server_interface.send_move(move_to_send)
            self.mensagem_label.config(text="Jogada enviada")

    # Definição de funções adicionais para manipulação de eventos
    def iniciar_partida(self):
        if self.tabuleiro.estado == 1:
            status_inicio = self.dog_server_interface.start_match(2)  # Inicia a partida com 2 jogadores
            if status_inicio.get_code() == "2":
                jogadores = status_inicio.get_players()
                if len(jogadores) >= 2:
                    message = status_inicio.get_message()  # Mensagem de início da partida
                    self.mensagem_label.config(text=message)  # Exibe a mensagem de início da partida
                    self.tabuleiro.comecar_partida(jogadores, status_inicio.get_local_id())
                    self.tabuleiro.set_estado(2)  # Define o estado da partida como 2 (preparação)
                    self.atualizar_interface()
                else:
                    self.mensagem_label.config(text="Erro: jogadores insuficientes")
            else:
                self.mensagem_label.config(text="Erro ao iniciar partida: " + status_inicio.get_message())
        else:
            self.mensagem_label.config(text="Você já está em uma partida")


   
    #MUDAR NO DIAGRAMA
    def receive_start(self, start_status):
        jogadores = start_status.get_players()
        if len(jogadores) >= 2:
            jogador_local_id = start_status.get_local_id()
            self.tabuleiro.comecar_partida(jogadores, jogador_local_id)
            self.tabuleiro.set_estado(2)  # Define o estado da partida como 2 (preparação)
            message = start_status.get_message()
            self.mensagem_label.config(text=message)
            self.atualizar_interface()
        else:
            self.mensagem_label.config(text="Erro: jogadores insuficientes")
        
        
    #MUDAR NO DIAGRAMA
    def receive_move(self, a_move):
        self.tabuleiro.receber_jogada(a_move)
        self.atualizar_interface()

    #MUDAR NO DIAGRAMA
    def receive_withdrawal_notification(self):
        self.tabuleiro.receber_desistencia()
        self.mensagem_label.config(text="Seu oponente desistiu!")
        self.atualizar_interface()
     
    def comprar_base(self):
        print("Botão Comprar Base clicado")  # Log do clique no console
        mensagem = self.tabuleiro.comprar_base()
        self.mensagem_label.config(text=mensagem)
        self.atualizar_interface()

    def tiro_preciso(self):
        print("Botão Tiro Preciso clicado")  # Log do clique no console

    def tiro_normal(self):
        print("Botão Tiro Normal clicado")  # Log do clique no console
        mensagem = self.tabuleiro.tiro_normal()
        self.mensagem_label.config(text=mensagem)
        self.atualizar_interface()

    def tiro_forte(self):
        print("Botão Tiro Forte clicado")  # Log do clique no console
        # Implementação do método tiro_forte

    # Outras funções que podem ser implementadas conforme necessário
    def atualizar_interface(self):
        self.saldo_label.config(text=f"Saldo: {self.tabuleiro.jogador_local.get_saldo()}")
