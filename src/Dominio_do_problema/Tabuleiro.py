
from Dominio_do_problema.Campo import Campo
from Dominio_do_problema.Canhao import Canhao
from Dominio_do_problema.Jogador import Jogador  # Importe Jogador diretamente se necessário

#class Tabuleiro(object):
class Tabuleiro:

    def __init__(self):
        self._jogador_remoto = Jogador()
        self._jogador_local = Jogador()
        self._campo_jogador_local = None
        self._status_partida = 1
        self._campo_jogador_remoto = Campo()
        self._canhao_jogador_local = Campo()
        self._canhao_jogador_remoto = Canhao()

        self._unnamed_JogadorInterface_ = None
        self._unnamed_ImagemInterface_ = None
        self._unnamed_Campo_ = []
        self._unnamed_Jogador_ = []
        self._unnamed_Canhao_ = []

    def tiro_normal(self):
        pass

    def get_status_partida(self):
        pass

    def comecar_partida(self, *aJogadores, aId_jogador_local, aJogadores2, aId_jogador_local2):
        pass

    def set_status_partida(self, aStatus):
        pass

    def ocupar_posicao(self, aLinha, aColuna):
        pass

    def diminuir_saldo_jogador(self, aSaldo):
        pass

    def aumentar_saldo_jogador(self, aSaldo):
        pass

    def verificar_saldo_jogador(self, aJogador):
        pass

    def receber_jogada(self, aA_move):
        pass

    def verificar_bases_colocadas_pelo_jogador(self, *aBases):
        pass

    def verificar_base_comprada(self, aLinha, aColuna):
        pass

    def verificar_tiro_normal(self, aLinha, aColuna):
        pass

    def verificar_tiro_forte(self, aLinha, aColuna):
        pass

    def verificar_tiro_preciso(self, aLinha, aColuna):
        pass

    def verificar_jogada_vencedora(self, aCampo_jogador):
        pass

    def definir_partida_finalizada(self):
        pass

    def gerar_item_jogada(self):
        pass

    def verificar_partida_andamento(self):
        pass

    def pega_campo_jogador_remoto(self):
        pass

    def identificar_posicao_atingida(self, aCampo_jogador_remoto, aPosicao_atingida):
        pass

    def calibrar_precisao_tiro_normal(self):
        pass

    def resetar_precisao_tiro_normal(self):
        pass

    def tiro_preciso(self):
        pass

    def tiro_forte(self):
        pass

    def verificar_numero_bases(self):
        pass

    def recupera_jogador_do_tiro_disparado_atraves_id_do_adversario(self, aId_jogador_dono_campo):
        pass

    def clicar_posicao_campo(self, aLinha, aColuna):
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
