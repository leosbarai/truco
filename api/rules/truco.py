class Truco:

    def __init__(self, table):
        self.table = table

    def table_match_value(self):
        if self.table.match_value < 3:
            score = 'TRUCO'
        elif 3 <= self.table.match_value < 6:
            score = 'SEIS'
        elif 6 <= self.table.match_value < 9:
            score = 'NOVE'
        elif 9 <= self.table.match_value < 11:
            score = 'DOZE'
        elif self.table.match_value == 11:
            return print('=> NÃO É PERMITIDO TRUCAR NA MÃO DE 11 <=')

        return print('ou tecle "S" se deseja pedir ' + score)

    # @classmethod
    # def bet(cls):
    #     players = cls.table.players
    #     for player in players:
    #         if player.my_turn:
