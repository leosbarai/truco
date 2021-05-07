from api.deck.cards import Cards
from api.deck.deliver_cards import DeliverCards
from api.deck.value_cards import get_value_cards
from api.players.players import Players


class Table:

    def __init__(self, players_qtt):
        self.players_qtt = players_qtt
        self.number_of_players_allowed = [2, 4, 6]
        self.players = []
        self.turned_card = []
        self.final_score = 12
        self.final_round = 2
        self.end_game = False

    def players_validate(self):
        while self.players_qtt not in self.number_of_players_allowed:
            print('Somente será permitida a participação de 2, 4 ou 6 jogadores!')
            self.players_qtt = int(input('Informe o número de participantes novamente: '))

    def players_create(self):
        players = 1
        while players <= self.players_qtt:
            name = input('Digite o nome do ' + str(players) + 'º jogador: ')
            player = Players()
            player.name = player.name_validate(name, players)
            self.players.append(player)
            players += 1

    def card_distribution(self):
        cards = DeliverCards(Cards.deck_of_cards_id())
        self.turned_card = cards.turn_card()
        for players in self.players:
            players.cards = get_value_cards(cards.player_cards(), self.turned_card)
