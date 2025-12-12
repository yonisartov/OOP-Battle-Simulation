from Electric import Electric
from Pokemon import Pokemon_Attributes
from math import floor

class Pikachu(Electric, Pokemon_Attributes):
    '''
    Class of pikachu pokemon.
    '''
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power, friendship):

        if not(isinstance(level, int) and isinstance(hit_points, int) and isinstance(attack_power, int) and isinstance(defense_power, int)):
            raise TypeError

        if not(level <= 32 and level >= 1 and hit_points >= 35 and hit_points <= 99 and defense_power >= 40 and defense_power <= 99 and attack_power >= 55 and attack_power <= 99 and friendship <= 5 and friendship >= 1):
            raise ValueError

        self.__friendship = friendship
        Electric.__init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power)


    def __repr__(self):
        return "The Pikachu " + self.get_name() + " of level " + str(self.get_level()) +" with " + str(self.get_hit_points()) + " HP"

    def abstract_def(self):
        pass
    def get_damage(self, other):
        if self.get_pokemon_type() in other.get_effective_against_me():
            return floor(((2*self.get_level()/5)+2)*(self.get_attack_power()/other.get_defense_power())*2) + self.__friendship

        return floor(((2*self.get_level()/5)+2)*(self.get_attack_power()/other.get_defense_power())*0.5) + self.__friendship

