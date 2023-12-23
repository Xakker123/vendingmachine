from ichimlik import Ichimlik
from vending_machin import VandingMachin

ichimlik1 = Ichimlik("Pepsi", "16000")
ichimlik2 = Ichimlik("Coca Cola", "16000")
ichimlik3 = Ichimlik("Suv", "2000")

vendingmachin = VandingMachin()
vendingmachin.addBeverage(ichimlik1)
vendingmachin = VandingMachin()
vendingmachin.addBeverage(ichimlik2)
vendingmachin = VandingMachin()
vendingmachin.addBeverage(ichimlik3)
