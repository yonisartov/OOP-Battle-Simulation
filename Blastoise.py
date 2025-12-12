import copy
from Water import Water
from Pokemon import Pokemon_Attributes
from math import floor
from Charmeleon import Charmeleon


class Blastoise(Water, Pokemon_Attributes):

    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):

        if not (isinstance(level, int) and isinstance(hit_points, int) and isinstance(attack_power, int) and isinstance(defense_power, int)):
            raise TypeError

        if not(level <= 50 and level >= 32 and hit_points >= 80 and hit_points <= 99 and defense_power >= 100 and defense_power <= 115 and attack_power >= 83 and attack_power <= 99):
            raise ValueError

        Water.__init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power)

    def __repr__(self):
        return "The Blastoise " + self.get_name() + " of level " + str(self.get_level()) + " with " + str(self.get_hit_points()) + " HP"

    def abstract_def(self):
        pass