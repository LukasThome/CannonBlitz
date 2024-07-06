
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
        self.campos_acertados_tiro_rodada = []


    

    def tiro_normal(self):
        print("Método tiro_normal do Tabuleiro foi chamado")
        mensagem = ""
        if not self.verificar_partida_andamento():
            mensagem = "A partida deve estar em andamento"
        elif not self.jogador_local.informar_turno():
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

            self.set_campos_acertados_tiro_rodada(linha, coluna)
            # Trocar turno
            self.trocar_turno()

        return mensagem



    def get_estado(self):
        return self.estado
    
    def set_campos_acertados_tiro_rodada(self, linha, coluna):
        self.campos_acertados_tiro_rodada.append((linha, coluna))
        
    def limpar_campos_acertados_tiro_rodada(self):
        self.campos_acertados_tiro_rodada = []

    def comecar_partida(self, jogadores, id_jogador_local):
        self.jogador_local.definir_nome(jogadores[0][0])
        self.jogador_local.definir_id(jogadores[0][1])
        self.jogador_remoto.definir_nome(jogadores[1][0])
        self.jogador_remoto.definir_id(jogadores[1][1])
        if jogadores[0][1] == id_jogador_local:
            self.jogador_local.set_turno(True)
            self.jogador_remoto.set_turno(False)
        else:
            self.jogador_local.set_turno(False)
            self.jogador_remoto.set_turno(True)

    def set_estado(self, a):
        self.estado = a
    
    def informar_turno(self): #AVALIAR SE PODE ESTAR AQUI
        return self.jogador_local.informar_turno()

    def ocupar_posicao(self, linha, coluna):
        self.campo_jogador_local.adicionar_base(linha, coluna)


    #ADICIONAR NO DIAGRAMA
    def verificar_bases_colocadas(self):
        return len(self.campo_jogador_local.obter_posicoes_com_base()) >= 5

    def adicionar_base(self, linha, coluna):
        if self.estado == 2:  # Verificar se o estado da partida é 2 (preparação)
            self.campo_jogador_local.adicionar_base(linha, coluna)
            if self.verificar_bases_colocadas():
                self.estado = 3  # Atualizar estado para 3 (em andamento)
        
    
    def diminuir_saldo_jogador(self, saldo):
        self.jogador_local.diminuir_saldo(saldo)

    def aumentar_saldo_jogador(self, saldo):
        self.jogador_local.aumentar_saldo_jogador(saldo)

    def verificar_saldo_jogador(self, jogador):
        return Jogador.get_saldo(jogador)

    def receber_jogada(self, a_move):
        move_type = a_move.get('type')
        if move_type == 'move':
            player_id = a_move.get('player_id')
            position = a_move.get('position')
            # Tratar a jogada aqui (ex: processar um tiro, etc.)
        elif move_type == 'initial_setup':
            positions = a_move.get('positions', [])
            for pos in positions:
                linha, coluna = pos
                self.campo_jogador_remoto.adicionar_base(linha, coluna)

    def verificar_bases_colocadas_pelo_jogador(self, Bases):#implementar
        return len(self.campo_jogador_local.obter_posicoes_com_base()) >= 5

    def verificar_base_comprada(self, linha, coluna):#implementar
        pass

    def verificar_tiro_normal(self, linha, coluna):#implementar
        pass

    def verificar_tiro_forte(self, linha, coluna):#implementar
        pass

    def verificar_tiro_preciso(self, linha, coluna):#implementar
        pass

    def verificar_jogada_vencedora(self, Campo_jogador): #implementar
        pass

    def definir_partida_finalizada(self): ##implementar
        pass

    def gerar_item_jogada(self):
            return {
                'type': 'move',
                'player_id': self.jogador_local.id,
                'position': self.ultima_posicao_tiro  # supondo que você armazena a última posição de tiro aqui
            }

    def verificar_partida_andamento(self):
        return self.estado == 3     #Mudar para 3 no release

    def pega_campo_jogador_remoto(self):
        pass

    def identificar_posicao_atingida(self, Campo_jogador_remoto, Posicao_atingida): #implementar
        pass

    def calibrar_precisao_tiro_normal(self): #Não sei se é necessario estar aqui tambem
        pass

    def resetar_precisao_tiro_normal(self):
        self.canhao_jogador_local.resetar_precisao_tiro_normal()

    def tiro_forte(self):
        mensagem = ""
        if not self.verificar_partida_andamento():
            mensagem = "A partida deve estar em andamento"
        elif not self.jogador_local.informar_turno():
            mensagem = "Não é seu turno"
        else:
            # Realiza o tiro forte e obtém as posições atingidas
            posicoes_atingidas = self.canhao_jogador_local.tiro_forte(self.campo_jogador_remoto)

            # Verificar se alguma das posições atingidas tem uma base
            bases_destruidas = 0
            for linha, coluna in posicoes_atingidas:
                if self.campo_jogador_remoto.posicao_tem_base(linha, coluna):
                    # Destruir a base do adversário
                    self.campo_jogador_remoto.remover_base(linha, coluna)
                    bases_destruidas += 1

            if bases_destruidas == 0:
                mensagem = "Você não destruiu nenhuma base."
            else:
                # Aumentar o saldo do jogador
                self.jogador_local.aumentar_saldo_jogador(bases_destruidas)
                mensagem = f"Você destruiu {bases_destruidas} base(s) adversária(s)!"

            # Adicionar todas as posições atingidas à lista de campos acertados nesta rodada
            for linha, coluna in posicoes_atingidas:
                self.set_campos_acertados_tiro_rodada(linha, coluna)

            # Verificar jogada vencedora
            if self.verificar_jogada_vencedora(self.campo_jogador_remoto):
                mensagem += " Você venceu o jogo!"

            # Trocar turno
            self.trocar_turno()

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

    def clicar_posicao_campo(self, linha, coluna): #ainda nao pronta
        if self.informar_turno():
            self.ocupar_posicao(linha, coluna)
            self.diminuir_saldo_jogador(1)
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

    def inicializar(self): #Provavelmente nao ira precisar
        pass

    def pegar_estadoCampo(self):
        pass

    def receber_desistencia(self):
        pass


    def saldo_suficiente(self, valor):
        return self.jogador_local.saldo_suficiente(valor)
    
    
    def trocar_turno(self):
        if self.jogador_local.informar_turno():
            self.jogador_local.set_turno(False)
            self.jogador_remoto.set_turno(True)
        else:
            self.jogador_local.set_turno(True)
            self.jogador_remoto.set_turno(False)
        print(f"Turno trocado. Turno do jogador local: {self.jogador_local.informar_turno()}, Turno do jogador remoto: {self.jogador_remoto.informar_turno()}")
