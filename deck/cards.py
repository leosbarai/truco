import requests


class Cards:

    @classmethod
    def deck_of_cards_id(cls):
        response = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?cards=AS,AD,AC,AH,2S,2D,2C,2H,3S,3D,'
                                '3C,3H,4S,4D,4C,4H,5S,5D,5C,5H,6S,6D,6C,6H,7S,7D,7C,7H,QS,QD,QC,QH,JS,JD,JC,JH,KS,KD,'
                                'KC,KH')

        if response.status_code == 200:
            return response.json()['deck_id']
        else:
            print(response.status_code)
            exit()
