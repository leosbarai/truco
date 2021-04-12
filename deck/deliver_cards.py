import requests


class DeliverCards:

    def get_cards(self, deck_id, quantity):
        cards = requests.get('https://deckofcardsapi.com/api/deck/' + str(deck_id) + '/draw/?count=' + str(quantity))

        if cards.status_code == 200:
            players_card = []

            for card in cards.json()['cards']:
                players_card.append(card.get('code'))

            return players_card
        else:
            print(cards.status_code)
            exit()

    def cards_value(self, value):
        switcher = {
            "QUEEN": 8,
            "JACK": 9,
            "KING": 10,
            "ACE": 11,
            2: 12,
            3: 13
        }
        return switcher.get(value, value)

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

    def turn_card(self, deck_id):
        return DeliverCards.get_cards(deck_id, 1)

    def player_cards(self, deck_id):
        return DeliverCards.get_cards(deck_id, 3)
