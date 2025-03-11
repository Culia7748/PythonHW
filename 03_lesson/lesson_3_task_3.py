from address import Address
from mailing import Mailing

to_address = Address("188664", "Токсово", "Буланова", "18", "2")
from_address = Address("410007", "Саратов", "Антонова", "33А","56")

mailing = Mailing("15364795", to_address, from_address, "1750")

print(mailing)