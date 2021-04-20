from deck.cards import Cards
from deck.deliver_cards import DeliverCards


class ValueCards:
    deck_id = Cards().deck_of_cards_id()
    turned_card = DeliverCards(deck_id).turn_card()
    player_one_cards = DeliverCards(deck_id).player_cards()
    player_two_cards = DeliverCards(deck_id).player_cards()

    print(turned_card)
    print(player_one_cards)
    print(player_two_cards)

    # for card in p1['cards']:
    #     card['value'] = cards_value(card.get('value'))

    def cards_value(self, value):
        switcher = {
            "QUEEN": 8,
            "JACK": 9,
            "KING": 10,
            "ACE": 11,
            2: 12,
            3: 13
        }
        return switcher.get(self, value, value)

    def suits_value(self, value):
        switcher = {
            "CLUBS": 400,
            "HEARTS": 300,
            "SPADES": 200,
            "DIAMONDS": 100
        }
        return switcher.get(value, value)

    def get_manilha(self, value):
        switcher = {
            "ACE": 2,
            2: 3,
            3: 4,
            4: 5,
            5: 6,
            7: "QUEEN",
            "QUEEN": "JACK",
            "JACK": "KING",
            "KING": "ACE"
        }
        return switcher.get(value)


    # def get_value_cards(player_cards):
    #
    #     for card in player_cards:
    #         if card.get('value')


