from deck.cards import Cards
from deck.deliver_cards import DeliverCards


def assigns_value_cards(cards):
    switcher = {
        "QUEEN": 8,
        "JACK": 9,
        "KING": 10,
        "ACE": 11,
        2: 12,
        3: 13
    }
    return switcher.get(cards, cards)


def suits_value(value):
    switcher = {
        'CLUBS': 400,
        'HEARTS': 300,
        'SPADES': 200,
        'DIAMONDS': 100
    }
    return switcher.get(value)


def get_manilha(value):
    switcher = {
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 7,
        7: 8,
        8: 9,
        9: 10,
        10: 1
    }
    return switcher.get(value)


def get_value_cards(player_cards, turned_card):
    manilha = get_manilha(int(turned_card[0].get('value')))

    for card in player_cards:
        card['value'] = assigns_value_cards(card.get('value'))

        if card['value'] == manilha:
            card['value'] = suits_value(card.get('suit'))

    return player_cards
