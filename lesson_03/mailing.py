from address import Address


class Mailing:
    def __init__(self, to_address: Address, from_address: Address,
                 cost: int, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} из {self.from_address.index}, "
                f"{self.from_address.city}, {self.from_address.street}, "
                f"{self.from_address.house} - {self.from_address.flat} "
                f"в {self.to_address.index}, {self.to_address.city}, "
                f"{self.to_address.street}, "
                f"{self.to_address.house} - {self.to_address.flat}. "
                f"Стоимость {self.cost} рублей.")
