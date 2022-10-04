from pip import main


class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    #ligar e desligar
    def power(self):
        if  self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    #mudança de canal
    def aumenta_canal(self):
        self.canal += 1
    def diminui_canal(self):
        self.canal -= 1


if __name__ == '__main__': 
    #quando quem tá me chamando, for do mesmo arquivo, eu faço o que tá embaixo. Senão, eu não faço nada
    #precisa fazer esse if se for teste no mesmo arquivo
    televisão = Televisão()

    ##Ligando e desligando a TV
    print('TV está ligada: {}' .format(televisão.ligada))

    televisão.power()
    print('TV está ligada: {}' .format(televisão.ligada))

    televisão.power()
    print('TV está ligada: {}' .format(televisão.ligada))

    televisão.power()
    print('TV está ligada: {}' .format(televisão.ligada))

    ##Canais
    print('Canal atual quando ligada: {}' .format(televisão.canal))

    televisão.aumenta_canal()
    televisão.aumenta_canal()
    print('Canal atual: {}' .format(televisão.canal))

    televisão.aumenta_canal()
    print('Canal atual: {}' .format(televisão.canal))

    televisão.diminui_canal()
    print('Canal atual: {}' .format(televisão.canal))