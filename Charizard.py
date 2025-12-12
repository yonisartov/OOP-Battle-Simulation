from Pokemon import Pokemon_Attributes
from Fire import Fire

class Charizard(Fire, Pokemon_Attributes):
    '''
    Class of Charizard pokemon.
    '''
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):

        if not(isinstance(level, int) and isinstance(hit_points, int) and isinstance(attack_power, int) and isinstance(defense_power, int)):
            raise TypeError

        if not(level <= 50 and level >= 32 and hit_points >= 78 and hit_points <= 99 and defense_power >= 78 and defense_power <= 99 and attack_power >= 84 and attack_power <= 99):
            raise ValueError

        Fire.__init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power)

    def __repr__(self):
        return "The Charizard " +self.get_name() + " of level " + str(self.get_level()) + " with " + str(self.get_hit_points()) + " HP"

    def abstract_def(self):
        pass