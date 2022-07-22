from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Light(Switchable):
    def turn_on(self):
        print('Switched on')

    def turn_off(self):
        print('Switched off')


class PowerSwitch:
    def __init__(self, c:Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
        else:
            self.client.turn_on()
            self.on = True


l = Light()
h = PowerSwitch(l)
h.press()