import textos

class SelecionarTextos:
    def __init__(self):
        self.textosObj = textos.textos

    def selecionarDificuldade(self, dificuldade):
        return [texto["texto"] for texto in self.textosObj if texto["dificuldade"] == dificuldade]
        #resultado = []
        #for texto in self.textosObj:
        #    if texto["dificuldade"] == dificuldade:
        #    resultado.append(texto["texto"])
        #return resultado

#selecao = SelecionarTextos()
#dificuldade_desejada = 2
#textos_filtrados = selecao.selecionarDificuldade(2)
#
#for texto in textos_filtrados:
#    print(texto)
