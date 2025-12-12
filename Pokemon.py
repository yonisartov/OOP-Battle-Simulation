from abc import ABC, abstractmethod
import copy
from math import floor

class Pokemon(ABC):
    '''
    Pokemon is the abstract class the everyone inherits from. has name and catch rate (which all pokemons has) and some
    methods all the pokemons has.
    '''

    def __init__(self, name, catch_rate):
        '''
        :param name: Name of the Pokemon -> string
        :param catch_rate: catch rate -> is between 40 and 45 include
        '''

        # Checking the type of name is str type, and type of catch rate is int type
        if not(isinstance(name, str) and isinstance(catch_rate, int)):
            raise TypeError
        self.__name = name
        # Checking the value of catch rate is between 40 and 45 include
        if catch_rate < 40 or catch_rate > 45:
            raise ValueError
        self.__catch_rate = catch_rate


    def get_name(self):
        return copy.copy(self.__name)

    def get_catch_rate(self):
        return copy.copy(self.__catch_rate)

    @abstractmethod
    def get_pokemon_type(self):
        pass

    @abstractmethod
    def get_effective_against_me(self):
        pass

    @abstractmethod
    def get_effective_against_others(self):
        pass

    @abstractmethod
    def get_level(self):
        pass
    @abstractmethod
    def get_hit_points(self):
        pass
    @abstractmethod
    def get_defense_power(self):
        pass

    @abstractmethod
    def get_attack_power(self):
        pass

    @abstractmethod
    def get_level(self):
        pass
    @abstractmethod
    def can_fight(self):
        pass
    @abstractmethod
    def get_damage(self):
        pass

    @abstractmethod
    def abstract_def(self):
        pass

    @abstractmethod
    def absorb(self):
        pass

    @abstractmethod
    def level_up(self, level_gain):
        pass



class Pokemon_Attributes(Pokemon):
    '''
    Extension class of pokemon with more attributes all the pokemons has. to prevent code duplications this class will
    gather all methods all pokemons has and do them once instead of writing them for each pokemon.
    '''
    def __init__(self, name, catch_rate, level, hit_points, attack_power, defense_power):
        Pokemon.__init__(self, name, catch_rate)
        self.__hit_points = hit_points
        self.__attack_power = attack_power
        self.__defense_power = defense_power
        self.__level = level
        self.__born_life = hit_points


    def get_level(self):
        return copy.copy(self.__level)
    def get_hit_points(self):
        return copy.copy(self.__hit_points)

    def get_defense_power(self):
        return copy.copy(self.__defense_power)

    def get_attack_power(self):
        return copy.copy(self.__attack_power)

    def can_fight(self):
        if int(self.__born_life*0.1) < self.__hit_points:
            return True
        return False

    def get_damage(self, other):
        if self.get_pokemon_type() in other.get_effective_against_me():
            base_damage = floor(((2*self.get_level()/5)+2)*(self.get_attack_power()/other.get_defense_power())*2)
        else:
            base_damage = floor(((2*self.get_level()/5)+2)*(self.get_attack_power()/other.get_defense_power())*0.5)

        if self.get_pokemon_type() == "fire":
            if self.get_level() <= 15:
                return base_damage
            elif self.get_level() >= 16 and self.get_level() <= 31:
                return base_damage + 2
            else:
                return base_damage + 4

        elif self.get_pokemon_type() == "water":
            if self.get_level() <= 15:
                return base_damage
            elif self.get_level() >= 16 and self.get_level() <= 31:
                return base_damage - 1
            else:
                return base_damage - 2

    def attack(self, other):
        if self.can_fight() and other.can_fight():
            self.__hit_points -= floor(self.__born_life*0.1)
            other.absorb(self.get_damage(other))


    def absorb(self, damage):
        self.__hit_points -= damage

    def level_up(self, level_gain):
        pokemon_type = self.get_pokemon_type()
        if pokemon_type == "fire" or pokemon_type == "water":
            if level_gain <= 16 and level_gain >= 1:
                if self.__level <= 15:
                    self.__level += level_gain
                    if self.__level > 15:
                        return self.evolve()
                elif self.__level >= 16 and self.__level <= 31:
                    self.__level += level_gain
                    if self.__level > 31:
                        return self.evolve()
                else:
                    if self.__level + level_gain > 50:
                        self.__level = 50
                    else:
                        self.__level += level_gain

        elif self.get_pokemon_type() == "electric":    #Electric
            if level_gain > 0:
                if self.__level + level_gain > 50:
                    self.__level = 50
                else:
                    self.__level += level_gain


    @abstractmethod
    def get_pokemon_type(self):
        pass

    @abstractmethod
    def abstract_def(self):
        pass

    @abstractmethod
    def get_effective_against_me(self):
        pass

    @abstractmethod
    def get_effective_against_others(self):
        pass











