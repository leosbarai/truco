from api.deck.cards import Cards
from api.deck.deliver_cards import DeliverCards
from api.deck.value_cards import get_value_cards
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

    cards = DeliverCards(Cards.deck_of_cards_id())

    turned_card = cards.turn_card()

    player1_cards = cards.player_cards()

    player2_cards = cards.player_cards()

    player1.cards = get_value_cards(player1_cards, turned_card)
    player2.cards = get_value_cards(player2_cards, turned_card)

    print('Vira: ')
    print(turned_card)
    print('Cartas do ' + player1.name + ': ')
    print(player1.cards)
    print('Cartas do ' + player2.name + ': ')
    print(player2.cards)
