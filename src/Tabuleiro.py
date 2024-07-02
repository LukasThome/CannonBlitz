
from Campo import Campo
from Canhao import Canhao
from Jogador import Jogador
import random
  

class Tabuleiro:

    def __init__(self):
        super().__init__()
        self.jogador_local = Jogador()
        self.jogador_remoto = Jogador()
        self.jogador_local.definir_nome("Jogador Local")  # Define o nome do jogador
        self.jogador_remoto.definir_nome("Jogador Remoto")  # Define o nome do jogador
        self.jogador_local.definir_id(1)         
        self.jogador_remoto.definir_id(2)
        self.estado = 1
        self.campo_jogador_local = Campo(1)
        self.campo_jogador_remoto = Campo(2)
        self.canhao_jogador_local = Canhao()
        self.canhao_jogador_remoto = Canhao()


    def tiro_normal(self):
        print("Método tiro_normal do Tabuleiro foi chamado")
        mensagem = ""
        if not self.verificar_partida_andamento():
            mensagem = "A partida deve estar em andamento"
        elif not self.informar_turno():  # Ajuste para usar o método correto
            mensagem = "Não é seu turno"
        else:
            # Identificar a posição que o tiro acertou
            linha, coluna = self.canhao_jogador_local.tiro_normal(self.campo_jogador_remoto)
            print(f"Posição atingida: ({linha}, {coluna})")

            # Verificar se a posição tem uma base
            if not self.campo_jogador_remoto.posicao_tem_base(linha, coluna):
                # Calibrar precisão
                self.canhao_jogador_local.calibrar_precisao()
                mensagem = "Você não acertou nenhuma base."
            else:
                # Destruir a base do adversário
                self.campo_jogador_remoto.remover_base(linha, coluna)
                # Aumentar o saldo do jogador
                self.jogador_local.aumentar_saldo_jogador(1)
                # Resetar precisão
                self.canhao_jogador_local.resetar_precisao_tiro_normal()
                mensagem = "Você destruiu uma base adversária!"

            # Verificar jogada vencedora
            if self.verificar_jogada_vencedora(self.campo_jogador_remoto):
                mensagem += " Você venceu o jogo!"

        return mensagem

    def get_estado(self):
        return self.estado

    def comecar_partida(self, jogadores, id_jogador_local):
        jogador_local_name = jogadores[0][0]
        jogador_local_id = jogadores[0][1]
        jogador_local_order = jogadores[0][2]
        jogador_remoto_name = jogadores[1][0]
        jogador_remoto_id = jogadores[1][1]
        if jogador_local_order == "1":
            self.jogador_local.set_turno(True)
        else:
            self.jogador_remoto.set_turno(False)
        self.set_estado(2)  

    def set_estado(self, a):
        self.estado = a
    
    def informar_turno(self): #AVALIAR SE PODE ESTAR AQUI
        return self.jogador_local.informar_turno()

    def ocupar_posicao(self, linha, coluna):
        self.campo_jogador_local.adicionar_base(linha, coluna)


    def diminuir_saldo_jogador(self, saldo):
        self.jogador_local.diminuir_saldo(saldo)

    def aumentar_saldo_jogador(self, saldo):
        self.jogador_local.aumentar_saldo_jogador(saldo)

    def verificar_saldo_jogador(self, jogador):
        return jogador.get_saldo()

    def receber_jogada(self, A_move):
        pass

    def verificar_bases_colocadas_pelo_jogador(self, Bases):
        pass

    def verificar_base_comprada(self, linha, coluna):
        pass

    def verificar_tiro_normal(self, linha, coluna):
        pass

    def verificar_tiro_forte(self, linha, coluna):
        pass

    def verificar_tiro_preciso(self, linha, coluna):
        pass

    def verificar_jogada_vencedora(self, Campo_jogador):
        pass

    def definir_partida_finalizada(self):
        pass

    def gerar_item_jogada(self):
        pass

    def verificar_partida_andamento(self):
        return self.estado == 1

    def pega_campo_jogador_remoto(self):
        pass

    def identificar_posicao_atingida(self, Campo_jogador_remoto, Posicao_atingida):
        pass

    def calibrar_precisao_tiro_normal(self):
        pass

    def resetar_precisao_tiro_normal(self):
        self.canhao_jogador_local.resetar_precisao_tiro_normal()

    def tiro_forte(self):
        mensagem = self.canhao_jogador_local.tiro_forte(self.campo_jogador_remoto)
        # Implementar lógica adicional conforme necessário
        return mensagem

    def verificar_numero_bases(self):
        return len(self.campo_jogador_local.obter_posicoes_com_base())

    def recupera_jogador_do_tiro_disparado_atraves_id_do_adversario(self, id_jogador_dono_campo):
        if id_jogador_dono_campo == self.jogador_local.id:
            return self.jogador_local
        elif id_jogador_dono_campo == self.jogador_remoto.id:
            return self.jogador_remoto
        else:
            return None

    def clicar_posicao_campo(self, linha, coluna):
        if self.informar_turno():
            self.ocupar_posicao(linha, coluna)
            self.aumentar_saldo_jogador(1)
            return f"Posição {linha}, {coluna} ocupada."
        else:
            return "Não é sua vez."

    def sortear_turno(self):
        turno = random.choice([True, False])
        self.jogador_local.set_turno(turno)
        self.jogador_remoto.set_turno(not turno)

    def comprar_base(self):
        mensagem = ""
        if not self.verificar_partida_andamento():
            mensagem = "A partida deve estar em andamento"
        elif not self.informar_turno():
            mensagem = "Não é seu turno"
        elif not self.saldo_suficiente(2):  # Supondo que o custo da base seja 2
            mensagem = "Saldo insuficiente"
        else:
            self.diminuir_saldo_jogador(2)
            mensagem = "Clique na posição desejada para colocar a base"
        
        return mensagem

    def inicializar(self):
        pass

    def pegar_estadoCampo(self):
        pass

    def receber_desistencia(self):
        pass


    def saldo_suficiente(self, valor):
        return self.jogador_local.saldo_suficiente(valor)