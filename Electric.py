from Pokemon import Pokemon_Attributes
from abc import ABC, abstractmethod
import copy

class Electric(Pokemon_Attributes):
    '''
    Class represents the electric pokemon type, inherits from Pokemon Attributes.
    with functions - Get type of pokemon - returns the pokemon type
    get effective against me - returns a list of pokemons effective against electric
    get effective against others - returns a list of effective pokemons against others
    '''
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):

        Pokemon_Attributes.__init__(self, name, catch_rate, level, hit_points, attack_power, defense_power)

        if not (isinstance(pokemon_type, str)):
            raise TypeError
        if pokemon_type != "electric":
            raise ValueError
        self.__pokemon_type = pokemon_type
        self.__effective_against_me = []
        self.__effective_against_others = ["water"]

    def get_pokemon_type(self):
        return copy.copy(self.__pokemon_type)

    def get_effective_against_me(self):
        return copy.copy(self.__effective_against_me)

    def get_effective_against_others(self):
        return copy.copy(self.__effective_against_others)

    @abstractmethod
    def abstract_def(self):
        pass