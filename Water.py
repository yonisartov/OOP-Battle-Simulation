from Pokemon import Pokemon_Attributes
from abc import ABC, abstractmethod
import copy

class Water(Pokemon_Attributes):
    '''
    Class of Water type pokemons.
    with functions - Get type of pokemon - returns the pokemon type
    get effective against me - returns a list of pokemons effective against Water
    get effective against others - returns a list of effective pokemons against others
    '''
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):

        Pokemon_Attributes.__init__(self, name, catch_rate, level, hit_points, attack_power, defense_power)

        if not (isinstance(pokemon_type, str)):
            raise TypeError
        if pokemon_type != "water":
            raise ValueError
        self.__pokemon_type = pokemon_type
        self.__effective_against_me = ["electric"]
        self.__effective_against_others = ["fire"]

    def get_pokemon_type(self):
        return copy.copy(self.__pokemon_type)

    def get_effective_against_me(self):
        return copy.copy(self.__effective_against_me)

    def get_effective_against_others(self):
        return copy.copy(self.__effective_against_others)

    @abstractmethod
    def abstract_def(self):
        pass