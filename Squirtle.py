import copy
from Water import Water
from Pokemon import Pokemon_Attributes
from math import floor
from Wartortle import Wartortle

class Squirtle(Water, Pokemon_Attributes):

        def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):

            if not(isinstance(level, int) and isinstance(hit_points, int) and isinstance(attack_power, int) and isinstance(defense_power, int)):
                raise TypeError

            if not(level <= 15 and level >= 1 and hit_points >= 44 and hit_points <= 58 and defense_power >= 65 and defense_power <= 79 and attack_power >= 48 and attack_power <= 62):
                raise ValueError

            Water.__init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power)

        def __repr__(self):
            return "The Squirtle "+self.get_name()+" of level "+str(self.get_level())+" with "+ str(self.get_hit_points())+ " HP"

        def evolve(self):
            '''
            evolving the pokemon and returning a new pokemon
            :return: a new pokemon
            '''
            if self.get_hit_points() + 15 < 59:
                new_hp = 59
            else:
                new_hp = self.get_hit_points() + 15

            return Wartortle(self.get_name(), self.get_catch_rate(), self.get_pokemon_type(), self.get_level(), new_hp, self.get_attack_power()+15, self.get_defense_power()+15)

        def abstract_def(self):
            pass