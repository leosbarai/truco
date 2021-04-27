class Players:

    def __init__(self, name=''):
        self.name = name
        self.cards = {}

    def name_validate(self, name, number):
        if name == '':
            self.name = 'Jogador_' + str(number)
            return self.name
        else:
            return name
