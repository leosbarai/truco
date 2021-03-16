from deck.cards import cards
from players.players import Players
from rules.deliver_cards import deliver_cards


class Game():
    player1 = Players("player_1")
    player2 = Players("player_2")

    deck_id = cards().deck_of_cards_id()

    player1.cards = deliver_cards().deliver_cards_to_players(deck_id, 3)
    player2.cards = deliver_cards().deliver_cards_to_players(deck_id, 3)

    print('{}: {}'.format(player1.user, player1.cards))
    print('{}: {}'.format(player2.user, player2.cards))
