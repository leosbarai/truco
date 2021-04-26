import requests

from api.deck.urls import URLs


class Cards:

    @classmethod
    def deck_of_cards_id(cls):
        response = requests.get(URLs.api_base + URLs.api_shuffle_cards + URLs.cards_list)

        if response.status_code == 200:
            print('Deck id retornado!')
            return str(response.json()['deck_id'])
        else:
            print("Erro no retorno" + response.status_code)
            exit()
