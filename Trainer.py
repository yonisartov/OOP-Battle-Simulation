import copy
from Pokemon import Pokemon
from math import floor



class Trainer():
    '''
    This class will build the Trainer figure in pokemon, with many attributes include list of pokemons, name (int),
    age(int) and exp(float). The trainer will have methods to catch pokemons and append them to his list of pokemons.
    '''

    def __init__(self, name, age, exp_modifier, pokemons_lst = None):

        if pokemons_lst == None:
            pokemons_lst = []
        if not(isinstance(name, str) and isinstance(age, int) and isinstance(exp_modifier, float) and isinstance(pokemons_lst, list)):
            raise TypeError
        if not(name != "" and age >= 16 and age <= 120 and exp_modifier > 1.5 and exp_modifier < 12.5):
            raise ValueError

        self.__name = name
        self.__age = age
        self.__exp_modifier = exp_modifier
        if pokemons_lst == None:
            self.__pokemons_lst = []
        else:
            if all([isinstance(i, Pokemon) for i in pokemons_lst]):
                self.__pokemons_lst = copy.deepcopy(pokemons_lst)


    def __len__(self):
        '''
        When asks for the len of trainer, will return the length of the pokemon list
        :return: len of pokemon lst.
        '''
        return len(self.__pokemons_lst)

    def __repr__(self):
        rstring = "The Trainer " + self.get_name() + " is " + str(self.get_age()) + " years old and has the following pokemons (" + str(len(self)) +" in total):\n"
        for pokemon in self.__pokemons_lst:
            rstring += '    '+pokemon.__repr__()+'\n'
        return rstring[:len(rstring)-1]

    def get_name(self):
        return copy.copy(self.__name)
    def get_age(self):
        return copy.copy(self.__age)

    def get_exp_modifier(self):
        return copy.copy(self.__exp_modifier)

    def get_pokemon_lst(self):
        return copy.deepcopy(self.__pokemons_lst)

    def change_pokemon_lst(self, pokemon, pokemon_id):
        self.__pokemons_lst[pokemon_id] = copy.deepcopy(pokemon)

    def catch_pokemon(self, pokemon):
        '''
        with a hard formula, it calculates the odds of the trainer to catch a pokemon with some variables taken into
        consideration.
        :param pokemon: The pokemon the trainer is trying to catch
        :return: doesn't return, but prints if the catch was successful or not. if it was appends to the pokemon list.
        '''
        capture_chances = pokemon.get_catch_rate()*self.get_exp_modifier()*((100-pokemon.get_hit_points())/100)
        if capture_chances > 50:
            self.__pokemons_lst.append(pokemon)
            print(self.get_name() + " caught " + pokemon.get_name())
        else:
            print(self.get_name() + " couldn't catch " + pokemon.get_name())

    def __eq__(self, other):
        '''
        Checks equality based on the sum of pokemons HP of each trainer
        :param other: Other Trainer object
        :return: True or False
        '''
        first_trainer = 0
        second_trainer = 0
        for pokemon1 in self.get_pokemon_lst():
            first_trainer += pokemon1.get_hit_points()
        for pokemon2 in other.get_pokemon_lst():
            second_trainer += pokemon2.get_hit_points()

        return first_trainer == second_trainer

    def __ne__(self, other):
        return not(self == other)

    def __gt__(self, other):    #Greater than
        first_trainer = 0
        second_trainer = 0
        for pokemon1 in self.get_pokemon_lst():
            first_trainer += pokemon1.get_hit_points()
        for pokemon2 in other.get_pokemon_lst():
            second_trainer += pokemon2.get_hit_points()
        if first_trainer > second_trainer:
            return True
        return False

    def __ge__(self, other):    #Greater or equal to
        first_trainer = 0
        second_trainer = 0
        for pokemon1 in self.get_pokemon_lst():
            first_trainer += pokemon1.get_hit_points()
        for pokemon2 in other.get_pokemon_lst():
            second_trainer += pokemon2.get_hit_points()
        if first_trainer >= second_trainer:
            return True
        return False

    def __lt__(self, other):    #Smaller than
        return not(self >= other)

    def __le__(self, other):    #Smaller or equal to
        return not(self > other)

    def __add__(self, other):
        new_name = ""
        new_lst = []
        if self >= other:
            new_name = self.get_name() + "-" + other.get_name()
            new_lst = self.get_pokemon_lst() + other.get_pokemon_lst()
        else:
            new_name = other.get_name() + "-" + self.get_name()
            new_lst = other.get_pokemon_lst() + self.get_pokemon_lst()
        age = floor((self.get_age() + other.get_age())/2)
        exp = (self.get_exp_modifier() + other.get_exp_modifier())/2
        return Trainer(new_name, age, exp, new_lst)


















