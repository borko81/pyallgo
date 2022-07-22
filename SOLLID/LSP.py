class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f'The vehicle name is {self.name}'

    def get_speed(self) ->str:
        return f'The vehicle speed is {self.speed}'


class Car(Vehicle):
    def start_engine(self) -> str:
        return f'Brumm'


c = Car('my car', 100)