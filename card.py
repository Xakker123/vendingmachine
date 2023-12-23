class Card:
    def __init__(self, card_id, card_credit) -> None:
        self.id = card_id
        self.credit = card_credit

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def credit(self):
        return self.credit

    @credit.setter
    def credit(self, value):
        self._credit = value
