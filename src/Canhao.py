from TiroNormal import TiroNormal
# from TiroPreciso import TiroPreciso
from TiroForte import TiroForte
from Campo import Campo

class Canhao:
    def __init__(self):
        self.tiro_normal_obj = TiroNormal()
        self.tiro_forte_obj = TiroForte()

    def resetar_precisao_tiro_normal(self):
        self.tiro_normal_obj.resetar_precisao()

    def calibrar_precisao(self):
        self.tiro_normal_obj.calibrar_precisao()

    def tiro_normal(self, campo_jogador_remoto: Campo):
        posicoes_com_base = campo_jogador_remoto.obter_posicoes_com_base()
        return self.tiro_normal_obj.atirar(posicoes_com_base)
    
    def tiro_forte(self, campo_jogador_remoto: Campo):
        posicoes = campo_jogador_remoto.get_posicoes()
        return self.tiro_forte_obj.atirar(posicoes)