from api.deck.cards import Cards
from api.deck.deliver_cards import DeliverCards
from api.deck.value_cards import get_value_cards, code_cards
from api.players.players import Players


class Game:
    print('''
            **********************************
                    Jogo de Truco!
            **********************************
    ''')

    name_p1 = input('Digite o nome do primeiro jogador: ')
    name_p2 = input('Digite o nome do segundo jogador: ')

    player1 = Players()
    player1.name = player1.name_validate(name_p1, 1)

    player2 = Players()
    player2.name = player2.name_validate(name_p2, 2)

    score_player1 = 0
    score_player2 = 0
    final_score = 12
    final_round = 2
    player1.my_turn = True
    round = 1

    while score_player1 < final_round or score_player2 < final_round:
        cards = DeliverCards(Cards.deck_of_cards_id())
        turned_card = cards.turn_card()
        player1_cards = cards.player_cards()
        player2_cards = cards.player_cards()

        player1.cards = get_value_cards(player1_cards, turned_card)
        player2.cards = get_value_cards(player2_cards, turned_card)

        print('********** ' + str(round) + 'ª RODADA **********')
        print('Tombo: ' + turned_card[0]['code'])

        while player1.not_played and player2.not_played:
            if player1.my_turn:
                cards = code_cards(player1.cards)
                print('Cartas do jogador ' + player1.name + ': ' + str(cards))
                chosen_card = str(input('Escolha uma carta: ')).upper()

                while chosen_card not in cards:
                    print('Cartas do jogador ' + player1.name + ': ' + str(cards))
                    chosen_card = str(input('Carta inválida, escolha novamente: ')).upper()

                for card in player1.cards:
                    if card['code'] == chosen_card:
                        value_card_p1 = card['value']
                        print('Carta ' + chosen_card + ' na mesa!')
                        # del (player1_cards[card])

                player1.not_played = False
                player1.not_played = False
            elif player2.my_turn:
                cards = code_cards(player2.cards)
                print('Cartas do jogador ' + player2.name + ': ' + str(cards))
                chosen_card = str(input('Escolha uma carta: ')).upper()

                while chosen_card not in cards:
                    print('Cartas do jogador ' + player2.name + ': ' + str(cards))
                    chosen_card = str(input('Carta inválida, escolha novamente: ')).upper()

                for card in player2.cards:
                    if card['code'] == chosen_card:
                        value_card_p2 = card['value']
                        print('Carta ' + chosen_card + ' na mesa!')
                        # del (player2_cards[card])

                player2.not_played = False
                player2.my_turn = False

        if value_card_p1 > value_card_p2:
            score_player1 += 1
            player1.my_turn = True
            player2.my_turn = False
            print('Jogador ' + player1.name + ' venceu a ' + round + 'ª rodada.')
        else:
            score_player2 += 1
            player1.my_turn = False
            player2.my_turn = True
            print('Jogador ' + player2.name + ' venceu a ' + round + 'ª rodada.')

        round += 1

    if score_player1 > score_player2:
        player1.winner_message()
    else:
        player2.winner_message()
