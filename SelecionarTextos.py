import textos

class SelecionarTextos:
    def __init__(self):
        self.textosObj = textos.textos

    def selecionarDificuldade(self, dificuldade):
        return [texto["texto"] for texto in self.textosObj if texto["dificuldade"] == dificuldade]

selecao = SelecionarTextos()
dificuldade_desejada = 2
textos_filtrados = selecao.selecionarDificuldade(2)

for texto in textos_filtrados:
    print(texto)
