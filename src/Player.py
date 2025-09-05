import time

from .Creature import Creature


class Player(Creature):

    def __init__(self,  name: str,  attack: int, defence: int, max_health: int, damage: tuple):
        super().__init__(name, attack, defence, max_health, damage)
        self.healing = 4

    def heal(self):
        if self.healing > 0:
            self.current_health += 0.3 * self.max_health
            if self.current_health > self.max_health:
                self.current_health = self.max_health
            time.sleep(1)
            print('Your current health:', self.current_health)
        else:
            time.sleep(1)
            print('You wasted all your healings...')

