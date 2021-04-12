from deck.cards import Cards
from deck.deliver_cards import DeliverCards


class ValueCards:
    deck_id = Cards().deck_of_cards_id()
    turned_card = DeliverCards.turn_card(deck_id)
    player_one_cards = DeliverCards.player_cards(deck_id)
    player_two_cards = DeliverCards.player_cards(deck_id)

    # for card in p1['cards']:
    #     card['value'] = cards_value(card.get('value'))

    def get_value_cards(self, ):