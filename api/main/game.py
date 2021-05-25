from api.rules.table import Table


class Game:
    print('''
            **********************************
                      Jogo de Truco!
            **********************************
    ''')

    players_qtt = int(input('Informe o número de participantes: '))
    table = Table(players_qtt)
    table.players_validate()
    table.players_create()
    table.play()
