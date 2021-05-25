from api.deck.cards import Cards
from api.deck.deliver_cards import DeliverCards
from api.deck.value_cards import get_value_cards, code_cards
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

    def play(self):
        while not self.end_game:
            self.card_distribution()
            round = 1
            value = 0
            while value < self.final_round:
                print('********** ' + str(round) + 'ª RODADA **********')
                print('Tombo: ' + self.turned_card[0]['code'])

                for player in self.players:
                    while not player.played:
                        cards = code_cards(player.cards)
                        print('Cartas do jogador ' + player.name + ': ' + str(cards))
                        chosen_card = str(input('Escolha uma carta: ')).upper()

                        while chosen_card not in cards:
                            print('Cartas do jogador ' + player.name + ': ' + str(cards))
                            chosen_card = str(input('Carta inválida, escolha novamente: ')).upper()

                        for card in player.cards:
                            if card['code'] == chosen_card:
                                player.card_value = int(card['value'])
                                print('Carta ' + chosen_card + ' na mesa!')
                                player.cards.remove(card)

                        player.played = True

                round_winner = max(self.players, key=lambda card: card.card_value)
                round_winner.score += 1
                print(round_winner.name + ' venceu a ' + str(round) + 'ª rodada.')

                for players in self.players:
                    players.played = False

                value = max(player.score for player in self.players)
                round += 1

            self.end_game = True
            self.winning_player()

    def winning_player(self):
        for players in self.players:
            if players.score == self.final_round:
                players.winner_message()
