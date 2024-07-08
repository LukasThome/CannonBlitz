
from Campo import Campo
from Canhao import Canhao
from Jogador import Jogador
import random
  

class Tabuleiro:

    def __init__(self):
        super().__init__()
        self.jogador_local = Jogador()
        self.jogador_remoto = Jogador()
        self.jogador_local.definir_id(1)         
        self.jogador_remoto.definir_id(2)
        self.estado = 1
        self.campo_jogador_local = Campo(1)
        self.campo_jogador_remoto = Campo(2)
        self.canhao_jogador_local = Canhao()
        self.canhao_jogador_remoto = Canhao()
        self.jogador_local_joga_primeiro = False

    def tiro_normal(self):
        mensagem = None
        linha, coluna = None, None
        partida_andamento = self.verificar_partida_andamento()
        if partida_andamento:
            vez_jogador_local = self.jogador_local.informar_turno()
            if vez_jogador_local:
                    self.jogador_local.set_turno(False)
                    self.jogador_remoto.set_turno(True)
                    campo_jogador_remoto = self.pega_campo_jogador_remoto()
                    linha, coluna = self.canhao_jogador_local.tiro_normal(campo_jogador_remoto)
                    posicao_tem_base = self.campo_jogador_remoto.posicao_tem_base(linha, coluna)
                    if posicao_tem_base:
                        self.campo_jogador_remoto.remover_base(linha, coluna)
                        self.jogador_local.aumentar_saldo_jogador(1)
                        self.canhao_jogador_local.resetar_precisao_tiro_normal()
                        mensagem = "Você destruiu uma base adversária!"
                        jogada_vencedora = self.verificar_jogada_vencedora(self.campo_jogador_remoto, self.jogador_local)
                        if jogada_vencedora:
                            mensagem += " Você venceu o jogo!"
                    else:
                        self.calibrar_precisao_tiro_normal()
                        mensagem = "Você não acertou nenhuma base."
            else:
                mensagem = "Não é seu turno"
        else:
            mensagem = "A partida deve estar em andamento! Inicie uma partida no menu principal"

        return mensagem,linha,coluna
    
    def tiro_preciso(self):
        mensagem = None
        linha, coluna = None, None
        partida_andamento = self.verificar_partida_andamento()
        if partida_andamento:
            vez_jogador_local = self.jogador_local.informar_turno()
            if vez_jogador_local:
                saldo_suficiente = self.jogador_local.saldo_suficiente(1)
                if saldo_suficiente:  
                    self.jogador_local.set_turno(False)
                    self.jogador_remoto.set_turno(True)
                    campo_jogador_remoto = self.pega_campo_jogador_remoto()
                    self.jogador_local.diminuir_saldo(1)
                    linha, coluna = self.canhao_jogador_local.tiro_preciso(campo_jogador_remoto)
                    posicao_tem_base = self.campo_jogador_remoto.posicao_tem_base(linha, coluna)
                    if posicao_tem_base:
                        self.campo_jogador_remoto.remover_base(linha, coluna)
                        self.jogador_local.aumentar_saldo_jogador(1)
                        mensagem = "Você destruiu uma base adversária!"
                        jogada_vencedora = self.verificar_jogada_vencedora(self.campo_jogador_remoto, self.jogador_local)
                        if jogada_vencedora:
                            mensagem += " Você venceu o jogo!"
                    else:
                        mensagem = "Você não acertou nenhuma base."
                else: 
                    mensagem = "Saldo insuficiente"
            else:
                mensagem = "Não é seu turno"
        else:
            mensagem = "A partida deve estar em andamento! Inicie uma partida no menu principal"
        return mensagem,linha,coluna
    
    def tiro_forte(self):
        mensagem = ""
        posicoes_atingidas = []
        partida_andamento = self.verificar_partida_andamento()
        vez_jogador_local = self.jogador_local.informar_turno()
        saldo_suficiente = self.jogador_local.saldo_suficiente(3)
        if not partida_andamento:
            mensagem = "A partida deve estar em andamento! Inicie uma partida no menu principal"
        elif not vez_jogador_local:
            mensagem = "Não é seu turno"
        elif not saldo_suficiente:
            mensagem = "Saldo insuficiente"
        else:
            campo_jogador_remoto = self.campo_jogador_remoto
            self.jogador_local.diminuir_saldo(3)
            posicoes_atingidas = self.canhao_jogador_local.tiro_forte(campo_jogador_remoto)

            bases_destruidas = 0
            for linha, coluna in posicoes_atingidas:
                posicao_tem_base = self.campo_jogador_remoto.posicao_tem_base(linha, coluna)
                if posicao_tem_base:
                    self.campo_jogador_remoto.remover_base(linha, coluna)
                    bases_destruidas += 1
            if bases_destruidas == 0:
                mensagem = "Você não destruiu nenhuma base, aguarde o turno do outro jogador"
            else:
                self.jogador_local.aumentar_saldo_jogador(bases_destruidas)
                mensagem = f"Você destruiu {bases_destruidas} base(s) adversária(s)! Aguarde o turno do outro jogador"
                partida_vencedora = self.verificar_jogada_vencedora(self.campo_jogador_remoto, self.jogador_local)
                if partida_vencedora:
                    mensagem += " Você venceu o jogo!"
            self.trocar_turno()
        return mensagem, posicoes_atingidas
        
    def get_estado(self):
        return self.estado
    
    def get_nome_jogador_local(self):
        return self.jogador_local.get_nome()

    def comecar_partida(self, jogadores):
        self.jogador_local.definir_nome(jogadores[0][0])
        self.jogador_local.definir_id(jogadores[0][1])
        self.jogador_remoto.definir_nome(jogadores[1][0])
        self.jogador_remoto.definir_id(jogadores[1][1])
        if jogadores[0][2] == '1':
            self.jogador_local_joga_primeiro = True


    def set_estado(self, status):
        self.estado = status
        if status == 3:
            if self.jogador_local_joga_primeiro:
                self.jogador_local.set_turno(True)
                self.jogador_remoto.set_turno(False)
            else:
                self.jogador_local.set_turno(False)
                self.jogador_remoto.set_turno(True)
    
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
        jogada = a_move.get('type')
        if jogada == 'colocar_bases':
            self.verificar_bases_colocadas_pelo_jogador(a_move.get('positions', []))
        elif jogada == 'comprar_base':
            return self.verificar_base_comprada(a_move.get('linha'), a_move.get('coluna'))
        elif jogada == 'tiro_normal':
            return self.verificar_tiro_normal(a_move.get('linha'), a_move.get('coluna'))
        elif jogada == 'tiro_preciso':
            return self.verificar_tiro_preciso(a_move.get('linha'), a_move.get('coluna'))
        elif jogada == 'tiro_forte':
            return self.verificar_tiro_forte(a_move.get('posicoes_atingidas'))

    def verificar_bases_colocadas_pelo_jogador(self, positions):
        for pos in positions:
            linha, coluna = pos
            self.campo_jogador_remoto.adicionar_base(linha, coluna)
        self.jogador_remoto.set_jogador_preencheu_bases()
        preencheu_bases = self.jogador_local.get_jogador_preencheu_bases()
        if preencheu_bases:
            self.set_estado(3)

    def verificar_base_comprada(self, linha, coluna):
        posicao = self.campo_jogador_remoto.pega_posicao(linha, coluna)
        posicao.set_defesa(True)
        self.jogador_remoto.diminuir_saldo(2)
        mensagem = "Jogador remoto comprou uma base, sua vez de jogar"
        self.jogador_local.set_turno(True)
        self.jogador_remoto.set_turno(False)
        return mensagem

    def verificar_tiro_normal(self, linha, coluna):
        posicao_tem_base = self.campo_jogador_local.posicao_tem_base(linha,coluna)
        if posicao_tem_base:
            self.campo_jogador_local.remover_base_atingida(linha,coluna)
            self.jogador_remoto.aumentar_saldo_jogador(1)
            self.canhao_jogador_remoto.resetar_precisao_tiro_normal()
            jogada_vencedora = self.verificar_jogada_vencedora(self.campo_jogador_local, self.jogador_remoto)
            if jogada_vencedora:
                mensagem = "Jogador remoto vencedor"
                return mensagem
            else:
                mensagem = "Jogador remoto acertou uma base sua! Sua vez de jogar"
        else:
            self.canhao_jogador_remoto.calibrar_precisao()
            mensagem = "Jogador remoto nao acertou nenhuma base, sua vez de jogar"
        self.jogador_local.set_turno(True)
        self.jogador_remoto.set_turno(False)
        return mensagem

    def verificar_tiro_forte(self, posicoes_atingidas):
        self.jogador_remoto.diminuir_saldo(3)
        bases_destruidas = 0
        for linha, coluna in posicoes_atingidas:
            posicao_tem_base = self.campo_jogador_local.posicao_tem_base(linha, coluna)
            if posicao_tem_base:
                self.campo_jogador_local.remover_base(linha, coluna)
                bases_destruidas += 1
        if bases_destruidas == 0:
            mensagem = "Jogador remoto nao acertou nenhuma base! Sua vez de jogar"
        else:
            self.jogador_remoto.aumentar_saldo_jogador(bases_destruidas)
            mensagem = f"Jogador remoto destruiu {bases_destruidas} base(s)! Sua vez de jogar"
            jogador_remoto_vencedor = self.verificar_jogada_vencedora(self.campo_jogador_local, self.jogador_remoto)
            if jogador_remoto_vencedor:
                mensagem = "Jogador remoto foi o vencedor"
                return mensagem
        self.jogador_local.set_turno(True)
        self.jogador_remoto.set_turno(False)
        return mensagem

    def verificar_tiro_preciso(self, linha, coluna):
        self.jogador_remoto.diminuir_saldo(1)
        posicao_tem_base = self.campo_jogador_local.posicao_tem_base(linha,coluna)
        if posicao_tem_base:
            self.campo_jogador_local.remover_base_atingida(linha,coluna)
            self.jogador_remoto.aumentar_saldo_jogador(1)
            self.canhao_jogador_remoto.resetar_precisao_tiro_normal()
            jogada_vencedora = self.verificar_jogada_vencedora(self.campo_jogador_local, self.jogador_remoto)
            if jogada_vencedora:
                mensagem = "Jogador remoto vencedor"
                return mensagem
            else:
                mensagem = "Jogador remoto acertou uma base! Sua vez de jogar"
        else:
            self.canhao_jogador_remoto.calibrar_precisao()
            mensagem = "Jogador remoto nao acertou nenhuma base! Sua vez de jogar"
        self.jogador_local.set_turno(True)
        self.jogador_remoto.set_turno(False)
        return mensagem

    def verificar_jogada_vencedora(self, campo_jogador_que_recebeu_tiros: Campo, jogador_que_atirou: Jogador):
        todas_bases_destruidas = not campo_jogador_que_recebeu_tiros.campo_tem_base()
        if todas_bases_destruidas:
            jogador_que_atirou.definir_jogador_vencedor()
            self.definir_partida_finalizada()
        return todas_bases_destruidas

    def definir_partida_finalizada(self):
        self.set_estado(4)

    def verificar_partida_andamento(self):
        return self.estado == 3     #Mudar para 3 no release

    def pega_campo_jogador_remoto(self):
        return self.campo_jogador_remoto

    def identificar_posicao_atingida(self, Campo_jogador_remoto, Posicao_atingida): #implementar/estamos usando posicao_tem_base do Campo -> Remover do VP
        pass

    def calibrar_precisao_tiro_normal(self):
        self.canhao_jogador_local.calibrar_precisao()

    def resetar_precisao_tiro_normal(self):
        self.canhao_jogador_local.resetar_precisao_tiro_normal()

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
        if self.campo_jogador_local.posicao_tem_base(linha,coluna):
            mensagem = "Posição ocupada"
        else:
            estado_partida = self.get_estado()
            match estado_partida:
                case 2:
                    if self.campo_jogador_local.pega_quantidade_bases() == 5:
                        mensagem = "Você adicionou todas as suas bases. Aguarde o outro jogador."
                    else:
                        self.campo_jogador_local.adicionar_base(linha, coluna)
                        mensagem = "Base adicionada! Clique em outra posição para adicionar outra base."
                case 3:
                    if self.jogador_local.get_comprando_base():
                        self.campo_jogador_local.adicionar_base(linha, coluna)
                        mensagem = "Base comprada adicionada! Aguarde o turno do outro jogador."
                        self.jogador_local.set_turno(False)
                        self.jogador_remoto.set_turno(True)
                    else:
                        mensagem = "Ação inválida"    
        return mensagem

    def sortear_turno(self):
        turno = random.choice([True, False])
        self.jogador_local.set_turno(turno)
        self.jogador_remoto.set_turno(not turno)

    def comprar_base(self):
        mensagem = ""
        if not self.verificar_partida_andamento():
            mensagem = "A partida deve estar em andamento! Inicie uma partida no menu principal"
        elif not self.informar_turno():
            mensagem = "Não é seu turno"
        elif not self.saldo_suficiente(2):
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
        self.set_estado(4)

    def saldo_suficiente(self, valor):
        return self.jogador_local.saldo_suficiente(valor)

    def trocar_turno(self):
        if self.jogador_local.informar_turno():
            self.jogador_local.set_turno(False)
            self.jogador_remoto.set_turno(True)
        else:
            self.jogador_local.set_turno(True)
            self.jogador_remoto.set_turno(False)

    def set_comprando_base(self, valor):
        self.jogador_local.comprando_base = valor
        
    def get_comprando_base(self):
        return self.jogador_local.comprando_base