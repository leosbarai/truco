from api.deck.cards import Cards
from api.deck.deliver_cards import DeliverCards
from api.deck.value_cards import get_value_cards, code_cards
from api.players.players import Players
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
    table.card_distribution()

    while score_player1 < final_round or score_player2 < final_round:
        print('********** ' + str(round) + 'ª RODADA **********')
        print('Tombo: ' + turned_card[0]['code'])

        while player1.not_played or player2.not_played:
            if player1.my_turn:
                cards = code_cards(player1.cards)
                print('Cartas do jogador ' + player1.name + ': ' + str(cards))
                chosen_card = str(input('Escolha uma carta: ')).upper()

                while chosen_card not in cards:
                    print('Cartas do jogador ' + player1.name + ': ' + str(cards))
                    chosen_card = str(input('Carta inválida, escolha novamente: ')).upper()

                for card in player1.cards:
                    if card['code'] == chosen_card:
                        value_card_p1 = int(card['value'])
                        print('Carta ' + chosen_card + ' na mesa!')
                        player1_cards.remove(card)

                player1.not_played = False  # criar função de jogador atual
                player1.my_turn = False
            else:
                cards = code_cards(player2.cards)
                print('Cartas do jogador ' + player2.name + ': ' + str(cards))
                chosen_card = str(input('Escolha uma carta: ')).upper()

                while chosen_card not in cards:
                    print('Cartas do jogador ' + player2.name + ': ' + str(cards))
                    chosen_card = str(input('Carta inválida, escolha novamente: ')).upper()

                for card in player2.cards:
                    if card['code'] == chosen_card:
                        value_card_p2 = int(card['value'])
                        print('Carta ' + chosen_card + ' na mesa!')
                        player2_cards.remove(card)

                player2.not_played = False
                player2.my_turn = False

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

    if score_player1 > score_player2:
        player1.winner_message()
    else:
        player2.winner_message()
