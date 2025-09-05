import time
from random import randint

from .constants import time_sleep


class Creature:
    def __init__(self, name: str,  attack: int, defence: int, max_health: int, damage: tuple):

        if attack > 30 or attack < 1:
            raise ValueError('Wrong attack value!')

        if defence > 30 or defence < 1:
            raise ValueError('Wrong defence value!')

        if max_health < 1:
            raise ValueError('It is impossible to generate creature with health bellow 1!')

        if len(damage) != 2:
            raise ValueError('Wrong length of damage interval!')

        if damage[0] < 1 or damage[1] < 1:
            raise ValueError('Damage can not be bellow 1!')

        if damage[0] > damage[1]:
            raise ValueError('First damage value should be lower then second!')

        self.name = name
        self.attack = attack
        self.defence = defence
        self.max_health = max_health
        self.current_health = max_health
        self.damage = damage
        self.is_alive = True

    def hit(self, opponent):

        attack_modifier = self.attack - opponent.defence + 1
        print(f'\t{self.name} attack {opponent.name} !')
        print(f'\tAttack modifier: {attack_modifier}')
        time.sleep(time_sleep)

        for num in range(attack_modifier):
            if opponent.is_alive:
                current_cubes = randint(1, 6)
                if current_cubes > 4:
                    print(f'\t\tRoll: {current_cubes}, good try!')
                    time.sleep(time_sleep)
                    damage_value = randint(self.damage[0], self.damage[1])
                    opponent.current_health -= damage_value
                    time.sleep(time_sleep)
                    print(
                        f'\t\t\tDamage: {damage_value}.', f'{opponent.name} health =',
                        f'{opponent.current_health}/{opponent.max_health}'
                    )
                    if opponent.current_health < 1:
                        opponent.is_alive = False
                        print(f'\t\t{opponent.name} is dead...')
                else:
                    print(f'\t\tRoll: {current_cubes}, bad try...')
                    time.sleep(time_sleep)
