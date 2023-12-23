from ichimlik import Ichimlik
from card import Card
from ustun import Ustun


class VandingMachin:
    def __init__(self) -> None:
        self.ichimliklar: list[Ichimlik] = []
        self.cards = {}
        # self.ustunlar: list[Ustun] = []
        self.ustunlar = {}

    def addBeverage(self, ichimlik:Ichimlik):
        self.ichimliklar.append(ichimlik)
        print(f"ichimlik qo'shildi {ichimlik}")

    def get_price(self, ichimlik_nomi):
        for ichimlik in self.ichimliklar:
            if ichimlik.nomi == ichimlik_nomi:
                return ichimlik.narxi
        return -1.0

    def recharge_card(self, card_id, credit):
        if card_id in self.cards.keys():
            self.cards[card_id] += credit
        else:
            self.cards[card_id] = credit

    def get_card(self, card_id):
        if card_id in self.cards.keys():
            return self.cards[card_id]
        else:
            return -1.0

    def refillcolum(self, ustunlar_soni, ichimlik_nomi):
        if ustunlar_soni in self.ustunlar.keys():
            self.ustunlar[ustunlar_soni] += ichimlik_nomi
            return self.ustunlar
        else:
            self.ustunlar[ustunlar_soni] = ichimlik_nomi









