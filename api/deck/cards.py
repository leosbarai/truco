from api.deck.urls import URLs

import logging
import requests as requests


class Cards:

    @classmethod
    def deck_of_cards_id(cls):
        response = requests.get(URLs.api_base + URLs.api_shuffle_cards + URLs.cards_list)

        if response.status_code == 200:
            logging.warning('Deck id retornado!')
            return str(response.json()['deck_id'])
        else:
            logging.warning("Erro no retorno" + str(response.status_code))
            exit()
