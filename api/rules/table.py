from api.deck.cards import Cards
from api.deck.deliver_cards import DeliverCards
from api.deck.value_cards import get_value_cards, code_cards
from api.players.players import Players
from api.rules.truco import Truco


class Table:

    def __init__(self, players_qtt):
        self.players_qtt = players_qtt
        self.number_of_players_allowed = [2, 4, 6]
        self.players = []
        self.turned_card = []
        self.final_score = 12
        self.final_round = 2
        self.end_game = False
        self.round = 1
        self.round_value = 0
        self.match_value = 1

    def players_validate(self):
        while self.players_qtt not in self.number_of_players_allowed:
            print('Somente será permitida a participação de 2, 4 ou 6 jogadores!')
            self.players_qtt = int(input('Informe o número de participantes novamente: '))

    def players_create(self):
        players = 1
        player_number = 0
        while players <= self.players_qtt:
            name = input('Digite o nome do ' + str(players) + 'º jogador: ')
            player = Players()
            player.name = player.name_validate(name, players)
            player_number += 1
            player.player_number = player_number
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
            self.erase_round()
            round_score = 1
            while self.round_value < self.final_round:
                print('********** ' + str(self.round) + 'ª RODADA **********')
                print('Tombo: ' + self.turned_card[0]['code'])

                for player in self.players:
                    while not player.played:
                        player.my_turn = True
                        cards = self.show_cards(player)

                        truco = Truco(self)
                        print('Escolha uma carta ', end="")
                        if self.match_value != 11:
                            print('ou tecle "S" para pedir ', end="")
                            print(truco.table_match_value())
                        else:
                            truco.table_match_value()

                        chosen_card = str(input('=> ')).upper()

                        if chosen_card[0] == 'S':
                            truco.bet()
                            self.show_cards(player)
                            chosen_card = str(input('=> ')).upper()
                        else:
                            while chosen_card not in cards:
                                print('Cartas do jogador ' + player.name + ': ' + str(cards))
                                chosen_card = str(input('Carta inválida, escolha novamente: ')).upper()

                        for card in player.cards:
                            if card['code'] == chosen_card:
                                player.card_value = int(card['value'])
                                print('Carta ' + chosen_card + ' na mesa!')
                                player.cards.remove(card)

                        player.played = True
                        player.my_turn = False

                round_winner = max(self.players, key=lambda card: card.card_value)
                round_winner.round_score += 1
                print(round_winner.name + ' venceu a ' + str(self.round) + 'ª rodada.')

                self.round_value = max(player.round_score for player in self.players)
                self.round += 1
                self.not_played()

            round_winner.score += round_score
            print(round_winner.name + ' = ' + str(round_winner.score))
            self.end_game = self.is_end_game()

    def show_cards(self, player):
        cards = code_cards(player.cards)
        print('Cartas do jogador ' + player.name + ': ' + str(cards))
        return cards

    def is_end_game(self):
        for players in self.players:
            if players.score >= self.final_score:
                players.winner_message()
                return True
            else:
                False

    def not_played(self):
        for players in self.players:
            players.played = False

    def erase_round(self):
        self.round = 1
        self.round_value = 0
        for players in self.players:
            players.round_score = 0
