from Posicao import Posicao
from Jogador import Jogador

class Campo:
    def __init__(self,id):
        self._id_jogador = id
        self.posicoes = []
        for y in range(3):
            column = []
            for x in range(5):
                column.append(Posicao(y, x,False))
            self.posicoes.append(column)

    def campo_tem_base(self):
        """@ReturnType boolean"""
        pass

    def remover_base_atingida(self, aLinha, aColuna):
        """@ParamType aLinha int
        @ParamType aColuna int
        @ReturnType void"""
        pass

    def obter_posicoes_com_base(self):
        """@ReturnType <"""
        pass

    def posicao_tem_base(self, aLinha, aColuna):
        """@ParamType aLinha int
        @ParamType aColuna int
        @ReturnType boolean"""
        pass

    def recupera_id_jogador(self):
        """@ReturnType int"""
        pass

    def pega_posicao(self, aLinha, aColuna):
        """@ParamType aLinha int
        @ParamType aColuna int
        @ReturnType Dominio do problema.Posicao"""
        pass

    def pega_quantidade_bases(self):
        """@ReturnType int"""
        pass
