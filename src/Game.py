import json
import time
from random import randint

from .Player import Player
from .Creature import Creature
from .constants import time_sleep


class Game:

    def __init__(self, num_of_enemies):
        if num_of_enemies < 1:
            raise ValueError('Wrong num of enemies (< 1)')
        self.enemies = Game.get_random_creatures(num_of_enemies)

    @staticmethod
    def get_random_creatures(amount: int) -> [Creature]:
        creatures = []
        with open('./tmp/monsters.json') as file:
            monster_dict = json.load(file)
            for i in range(amount):
                random_index = randint(0, len(monster_dict['types'])-1)
                current_creature = Game._dict_to_creature(monster_dict['types'][random_index])
                creatures.append(current_creature)
        return creatures

    @staticmethod
    def _dict_to_creature(creature_dict: dict) -> Creature:
        return Creature(
            name=creature_dict['name'],
            attack=creature_dict['attack'],
            defence=creature_dict['defence'],
            max_health=creature_dict['max_health'],
            damage=creature_dict['damage']
        )

    @staticmethod
    def _dict_to_player(player_dict: dict) -> Player:
        return Player(
            name=player_dict['name'],
            attack=player_dict['attack'],
            defence=player_dict['defence'],
            max_health=player_dict['max_health'],
            damage=player_dict['damage']
        )

    def play(self):

        with open('./tmp/player_settings.json') as file:
            player_dict = json.load(file)
            player = Game._dict_to_player(player_dict)

        for enemy in self.enemies:
            print('-------------------------------------')
            print(f'You faced with {enemy.name}')
            time.sleep(time_sleep)

            while True:
                time.sleep(time_sleep)
                print(f'\nYour health: {player.current_health}')
                print('Chose your action: if 1 - Heal, else - Hit')
                action = input()
                if action == '1':
                    player.heal()
                else:
                    player.hit(enemy)

                if not enemy.is_alive:
                    time.sleep(time_sleep)
                    print(f'{enemy.name} has been killed!')
                    break

                time.sleep(1)
                print(f'\n{enemy.name} is attacking you!')
                enemy.hit(player)

                if not player.is_alive:
                    time.sleep(time_sleep)
                    print('You die...')
                    print('Game over')
                    return

