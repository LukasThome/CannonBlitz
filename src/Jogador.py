class Jogador:
    
    def __init__(self):
        self.nome = None
        self.vencedor = False
        self.turno = True
        self.saldo = 5 # Mudar para 0 para release
        self.id = None
        self.preencheu_bases = False

    def definir_nome(self, nome):
        self.nome = nome

    def definir_id(self, id):
        self.id = id

    def informar_turno(self):
        return self.turno

    def definir_jogador_vencedor(self):
        self.vencedor = True

    def aumentar_saldo_jogador(self, saldoAcrescimo):
        self.saldo += saldoAcrescimo

    def saldo_suficiente(self, aSaldo_necessario):
        return self.saldo >= aSaldo_necessario

    def diminuir_saldo(self, saldoDecremento):
        self.saldo -= saldoDecremento

    def get_saldo(self):
        return self.saldo

    def set_turno(self, aTurno):
        self.turno = aTurno

    def set_vencedor(self):
        self.vencedor = True

    def get_jogador_preencheu_bases(self):
        return self.preencheu_bases
    
    def set_jogador_preencheu_bases(self):
        self.preencheu_bases = True

    def definir_jogador_vencedor(self):
        self.vencedor = True
    
    def get_nome(self):
        return self.nome
