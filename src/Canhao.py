from TiroNormal import TiroNormal
# from TiroPreciso import TiroPreciso
from TiroForte import TiroForte

class Canhao:
    def __init__(self):
        self.tiro_normal_obj = TiroNormal()
        self.tiro_forte_obj = TiroForte()

    def resetar_precisao_tiro_normal(self):
        self.tiro_normal_obj.resetar_precisao()

    def calibrar_precisao(self):
        self.tiro_normal_obj.calibrar_precisao()

    def tiro_normal(self, campo_jogador_remoto):
        print("Método tiro_normal do Canhao foi chamado")
        posicoes_com_base = campo_jogador_remoto.obter_posicoes_com_base()
        print(f"Posições com base: {posicoes_com_base}")
        return self.tiro_normal_obj.atirar(posicoes_com_base)
    
    def tiro_forte(self, campo_jogador_remoto):
        posicoes = campo_jogador_remoto.posicoes
        return self.tiro_forte_obj.atirar(posicoes)