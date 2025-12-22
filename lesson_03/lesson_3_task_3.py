from address import Address
from mailing import Mailing


to_address = Address("622056", "Простоквашино", "Медовая", 26, 58)
from_address = Address("623568", "Мурманск", "Ленина", 39, 45)
cost = 15
track = 63656
my_mailing = Mailing(to_address, from_address, cost, track)

print(my_mailing)
