import copy
from Fire import Fire
from Pokemon import Pokemon_Attributes
from math import floor
from Charmeleon import Charmeleon

class Charmander(Fire, Pokemon_Attributes):
    '''
    Class of Charizard pokemon.
    '''
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):

        if not(isinstance(level, int) and isinstance(hit_points, int) and isinstance(attack_power, int) and isinstance(defense_power, int)):
            raise TypeError

        if not(level <= 15 and level >= 1 and hit_points >= 39 and hit_points <= 57 and defense_power >= 43 and defense_power <= 57 and attack_power >= 52 and attack_power <= 63):
            raise ValueError

        Fire.__init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power)


    def __repr__(self):
        return "The Charmander "+self.get_name()+" of level "+str(self.get_level())+" with "+ str(self.get_hit_points())+ " HP"

    def get_damage(self, other):
        if self.get_pokemon_type() in other.get_effective_against_me():
            return floor(((2 * self.get_level() / 5) + 2) * (self.get_attack_power() / other.get_defense_power()) * 2)
        else:
            return floor(((2 * self.get_level() / 5) + 2) * (self.get_attack_power() / other.get_defense_power()) * 0.5)

    def evolve(self):
        if self.get_hit_points() + 19 < 58:
            new_hp = 58
        else:
            new_hp = self.get_hit_points() + 19

        return Charmeleon(self.get_name(), self.get_catch_rate(), self.get_pokemon_type(), self.get_level(), new_hp, self.get_attack_power()+12, self.get_defense_power()+15)

    def abstract_def(self):
        pass