
from Campo import Campo
from Canhao import Canhao
from Jogador import Jogador  

class Tabuleiro:

    def __init__(self):
        super().__init__()
        self._jogador_local = Jogador()
        self._jogador_remoto = Jogador()
        self._jogador_local.definir_nome("Jogador Local")  # Define o nome do jogador
        self._jogador_remoto.definir_nome("Jogador Remoto")  # Define o nome do jogador
        self._jogador_local.definir_id(1)             
        self._jogador_remoto.definir_id(2)
    
        self._campo_jogador_local = None
        self._estado = 1
        self._campo_jogador_remoto = Campo()
        self._canhao_jogador_local = Campo()
        self._canhao_jogador_remoto = Canhao()

        # self._unnamed_JogadorInterface_ = None
        # self._unnamed_ImagemInterface_ = None
        # self._unnamed_Campo_ = []
        # self._unnamed_Jogador_ = []
        # self._unnamed_Canhao_ = []

    def tiro_normal(self):
        pass

    def get_estado(self):
        return self._estado

    def comecar_partida(self, Jogadores, Id_jogador_local, Jogadores2, Id_jogador_local2):
        pass

    def set_estado(self, a):
        self._estado = a
        

    def ocupar_posicao(self, linha, coluna):
        pass

    def diminuir_saldo_jogador(self, saldo):
        pass

    def aumentar_saldo_jogador(self, saldo):
        pass

    def verificar_saldo_jogador(self, Jogador):
        pass

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
        pass

    def pega_campo_jogador_remoto(self):
        pass

    def identificar_posicao_atingida(self, Campo_jogador_remoto, Posicao_atingida):
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

    def recupera_jogador_do_tiro_disparado_atraves_id_do_adversario(self, Id_jogador_dono_campo):
        pass

    def clicar_posicao_campo(self, linha, coluna):
        pass

    def sortear_turno(self):
        pass

    def comprar_base(self):
        pass

    def inicializar(self):
        pass

    def pegar_estadoCampo(self):
        pass

    def receber_desistencia(self):
        pass
