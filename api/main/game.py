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
        while table.round < table.final_round:
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
                            player.card_value = int(card['value'])
                            print('Carta ' + chosen_card + ' na mesa!')
                            player.cards.remove(card)

                    player.played = True

            round_winner = max(table.players, key=lambda card: card.card_value)
            round_winner.score += 1
            print('Jogador ' + round_winner.name + ' venceu a ' + str(table.round) + 'ª rodada.')

            for players in table.players:
                players.played = False

            table.round += 1

    for players in table.players:
        if players.score == table.final_round:
            players.winner_message()
            table.end_game = True
