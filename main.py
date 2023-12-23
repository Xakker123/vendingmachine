from ichimlik import Ichimlik
from vending_machin import VandingMachin

ichimlik1 = Ichimlik("pepsi", "16000")
# ichimlik2 = Ichimlik("coca cola", "16000")
# ichimlik3 = Ichimlik("suv", "2000")

vendingmachin = VandingMachin()
vendingmachin.addBeverage(ichimlik1)
# vendingmachin = VandingMachin()
# vendingmachin.addBeverage(ichimlik2)
# vendingmachin = VandingMachin()
# vendingmachin.addBeverage(ichimlik3)
print(vendingmachin.get_price("suv"))
vendingmachin.recharge_card(1, 10000)
vendingmachin.recharge_card(1, 2000)
vendingmachin.recharge_card(2, 20000)
print(vendingmachin.cards)
print(vendingmachin.get_card(1))
print(vendingmachin.get_card(2))
print(vendingmachin.get_card(3))
vendingmachin.refillcolum(1, "pepsi")
print(vendingmachin.ustunlar)