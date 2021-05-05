from api.deck.value_cards import code_cards
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

    while not table.end_game:
        table.card_distribution()
        print('********** ' + str(table.round) + 'ª RODADA **********')
        print('Tombo: ' + table.turned_card[0]['code'])

        for player in table.players:
            while not player.played:
                cards = code_cards(player.cards)
                print('Cartas do jogador ' + player.name + ': ' + str(cards))
                chosen_card = str(input('Escolha uma carta: ')).upper()

                while chosen_card not in cards:
                    print('Cartas do jogador ' + player.name + ': ' + str(cards))
                    chosen_card = str(input('Carta inválida, escolha novamente: ')).upper()

                for card in player.cards:
                    if card['code'] == chosen_card:
                        player.value_card = int(card['value'])
                        print('Carta ' + chosen_card + ' na mesa!')
                        player.cards.remove(card)

                player.played = True

        if value_card_p1 > value_card_p2:
            score_player1 += 1
            player1.my_turn = True
            player2.my_turn = False
            print('Jogador ' + player1.name + ' venceu a ' + str(round) + 'ª rodada.')
        else:
            score_player2 += 1
            player1.my_turn = False
            player2.my_turn = True
            print('Jogador ' + player2.name + ' venceu a ' + str(round) + 'ª rodada.')

        player1.not_played = True
        player2.not_played = True
        round += 1

        for players in table.players:
            if players.score == table.final_round:
                players.winner_message()
                table.end_game = True
