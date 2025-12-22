from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy a40", "8912"),
    Smartphone("POCO", "X6", "8922"),
    Smartphone("Redmi", "A5", "8960"),
    Smartphone("OPPO", "A5", "8902"),
    Smartphone("Meizu", "Mblu 22", "8919")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
