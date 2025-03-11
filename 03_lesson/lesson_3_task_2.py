from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "L-123", 8_931_345_55_55),
    Smartphone("LG", "AAAA", 8_927_145_44_34),
    Smartphone("Samsung", "JPT-8", 8_999_143_21_12),
    Smartphone("Philips", "A35", 8_991_147_33_33),
    Smartphone("Simens", "NB-11", 8_323_555_44_33),
]

for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model}. {Smartphone.number}")