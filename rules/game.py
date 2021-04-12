class Game:
    # player1 = Players("player_1")
    # player2 = Players("player_2")
    #
    # deck_id = cards().deck_of_cards_id()
    #
    # player1.cards = deliver_cards().deliver_cards_to_players(deck_id, 3)
    # player2.cards = deliver_cards().deliver_cards_to_players(deck_id, 3)
    #
    # print('{}: {}'.format(player1.user, player1.cards))
    # print('{}: {}'.format(player2.user, player2.cards))




    
    p1 = {'success': True, 'deck_id': 'sdx30kwyqof9', 'cards': [
        {'code': '6S', 'image': 'https://deckofcardsapi.com/static/img/6S.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/6S.svg',
                    'png': 'https://deckofcardsapi.com/static/img/6S.png'}, 'value': '6', 'suit': 'SPADES'},
        {'code': 'KS', 'image': 'https://deckofcardsapi.com/static/img/KS.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/KS.svg',
                    'png': 'https://deckofcardsapi.com/static/img/KS.png'}, 'value': 'KING', 'suit': 'SPADES'},
        {'code': '4S', 'image': 'https://deckofcardsapi.com/static/img/4S.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/4S.svg',
                    'png': 'https://deckofcardsapi.com/static/img/4S.png'}, 'value': '4', 'suit': 'SPADES'}],
          'remaining': 37}

    # p2 = {'success': True, 'deck_id': 'sdx30kwyqof9', 'cards': [{'code': '6H', 'image': 'https://deckofcardsapi.com/static/img/6H.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/6H.svg', 'png': 'https://deckofcardsapi.com/static/img/6H.png'}, 'value': '6', 'suit': 'HEARTS'}, {'code': '4D', 'image': 'https://deckofcardsapi.com/static/img/4D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/4D.svg', 'png': 'https://deckofcardsapi.com/static/img/4D.png'}, 'value': '4', 'suit': 'DIAMONDS'}, {'code': '5D', 'image': 'https://deckofcardsapi.com/static/img/5D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/5D.svg', 'png': 'https://deckofcardsapi.com/static/img/5D.png'}, 'value': '5', 'suit': 'DIAMONDS'}], 'remaining': 34}

    # print(p1['cards'][0]['code'])
    # print(p1['cards'][1]['code'])
    # print(p1['cards'][2]['code'])

    # for card in p1['cards']:
    #     p1_cards[card.get('code')] = card.get('value')

    # for card in p1['cards']:
    #     p1_cards[card.get('code')] = cards_value(card.get('value'))

    for card in p1['cards']:
        card['value'] = cards_value(card.get('value'))

    print(p1['cards'])

    print(p1['cards'][0]['value'])
    print(p1['cards'][1]['value'])
    print(p1['cards'][2]['value'])
