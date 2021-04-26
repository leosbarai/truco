import requests

from api.deck.urls import URLs


class DeliverCards:

    def __init__(self, deck_id):
        self._deck_id = deck_id

    def get_cards(self, quantity):
        cards = requests.get(URLs.api_base + self._deck_id + URLs.api_base_count
                             + str(quantity))

        if cards.status_code == 200:
            print('Cartas retornadas!')
            return cards.json()['cards']
        else:
            print("Erro no retorno: " + str(cards.status_code))
            exit()

    def turn_card(self):
        return self.get_cards(1)

    def player_cards(self):
        return self.get_cards(3)