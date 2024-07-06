from TiroNormal import TiroNormal

class Canhao:
    def __init__(self):
        self.tiro_normal_obj = TiroNormal()

    def resetar_precisao_tiro_normal(self):
        self.tiro_normal_obj.resetar_precisao()

    def calibrar_precisao(self):
        self.tiro_normal_obj.calibrar_precisao()

    def tiro_normal(self, campo_jogador_remoto):
        posicoes_com_base = campo_jogador_remoto.obter_posicoes_com_base()
        return self.tiro_normal_obj.atirar(posicoes_com_base)
