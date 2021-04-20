import requests


class DeliverCards:

    def __init__(self, deck_id):
        self._deck_id = deck_id

    def get_cards(self, quantity):
        cards = requests.get('https://deckofcardsapi.com/api/deck/' + str(self._deck_id) + '/draw/?count='
                             + str(quantity))

        if cards.status_code == 200:
            return cards.json()['cards']
        else:
            print(cards.status_code)
            exit()

    def turn_card(self):
        return self.get_cards(1)

    def player_cards(self):
        return self.get_cards(3)
