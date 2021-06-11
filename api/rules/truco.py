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

        return score

    def truco_value(self, score):
        switcher = {
            'TRUCO': 3,
            'SEIS': 6,
            'NOVE': 9,
            'DOZE': 12
        }
        return switcher.get(score)

    def gambling_2players(self, value):
        switcher = {
            1: 2,
            2: 1
        }
        return switcher.get(value)

    def bet(self):

        for player in self.table.players:
            if player.my_turn:
                gambler_player = player.player_number
                receiving_player = self.gambling_2players(player.player_number)

                response = self.gamble(receiving_player)
                print(response)

    def gamble(self, player_gambler):
        for player in self.table.players:
            if player.player_number == player_gambler:
                print("Jogador: " + player.name)
                print("Aceita o pedido de ", end="")
                print(self.table_match_value() + "?")
                print('Digite "S" para aceitar ou "N" para correr: ')
                choice = str(input('==> ').upper())

                if choice[0] == 'S':
                    self.table.round_value = self.truco_value(self.table_match_value())
                    next_value = self.table_match_value()
                    print('Deseja pedir ' + next_value + '? Digite "S" para aceitar ou "N" para seguir com o jogo.')
                    response = str(input('==> ').upper())
                    return response
                else:
                    exit()
