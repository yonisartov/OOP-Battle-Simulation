from Pokemon import Pokemon_Attributes
from Fire import Fire
from Charizard import Charizard

class Charmeleon(Fire, Pokemon_Attributes):

    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):

        if not(isinstance(level, int) and isinstance(hit_points, int) and isinstance(attack_power, int) and isinstance(defense_power, int)):
            raise TypeError

        if not(level <= 31 and level >= 16 and hit_points >= 58 and hit_points <= 77 and defense_power >= 58 and defense_power <= 77 and attack_power >= 64 and attack_power <= 83):
            raise ValueError

        Fire.__init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power)

    def __repr__(self):
        return "The Charmeleon " +self.get_name() + " of level " + str(self.get_level()) + " with " + str(self.get_hit_points()) + " HP"


    def evolve(self):
        if self.get_hit_points() + 20 < 78:
            new_hp = 78
        else:
            new_hp = self.get_hit_points() + 20

        return Charmeleon(self.get_name(), self.get_catch_rate(), self.get_pokemon_type(), self.get_level(), new_hp, self.get_attack_power() + 20, self.get_defense_power() + 20)

    def abstract_def(self):
        pass