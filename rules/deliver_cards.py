import requests


class deliver_cards():

    def deliver_cards_to_players(self, deck_id, quantity):
        cards = requests.get('https://deckofcardsapi.com/api/deck/' + str(deck_id) + '/draw/?count=' + str(quantity))

        if cards.status_code == 200:
            players_card = []

            for card in cards.json()['cards']:
                players_card.append(card.get('code'))

            return players_card
        else:
            print(cards.status_code)
            exit()
