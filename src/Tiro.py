class Tiro:
    def __init__(self):
        self.chance_acerto = 0
        self.area_acerto = 0

    def atirar(self, posicoes_com_base):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses")
