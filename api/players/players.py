class Players:

    def __init__(self, name=''):
        self.name = name
        self.cards = {}
        self.my_turn = False

    def name_validate(self, name, number):
        if name == '':
            self.name = 'Jogador_' + str(number)
            return self.name
        else:
            return name

    def winner_message(self):
        print("Parabéns, " + self.name + "você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")