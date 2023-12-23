from ichimlik import Ichimlik


class VandingMachin:
    def __init__(self) -> None:
        self.ichimliklar: list[Ichimlik] = []

    def addBeverage(self, ichimlik:Ichimlik):
        self.ichimliklar.append(ichimlik)
        print(f"ichimlik qo'shildi {ichimlik}")

    def getprice(self, ichimlik):
        






