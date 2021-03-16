class Players():

    def __init__(self, user):
        self.user = user
        self.cards = []

    def __str__(self):
        _str = self.user
        return _str