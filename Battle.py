from Trainer import Trainer


class Battle:
    ''''Battle class - gets two trainers from class trainer,
        and make them battle between each other.
    '''
    def __init__(self, trainer1, trainer2):
        if not(isinstance(trainer1, Trainer) and isinstance(trainer2, Trainer)):
            raise TypeError

        self.__trainer1 = trainer1
        self.__trainer2 = trainer2

    def dual_battle(self, trainer1_pokemon_id, trainer2_pokemon_id):
        ''' Dual battle will help Total battle method to do the fight.
        :param trainer1_pokemon_id: the index of the pokemon on the list of pokemons of trainer 1
        :param trainer2_pokemon_id: the index of the pokemon on the list of pokemons of trainer 2
        :return: returns a tupple , first position of the tupple is number of rounds, second position is 0-tie,
         1-pokemon 1 win and 2-pokemon 2 wins.
        '''
        pokemon1_can_fight = self.__trainer1.get_pokemon_lst()[trainer1_pokemon_id].can_fight()
        pokemon2_can_fight = self.__trainer2.get_pokemon_lst()[trainer2_pokemon_id].can_fight()

        if not(pokemon1_can_fight or pokemon2_can_fight):
            return (0,0)
        elif not(pokemon1_can_fight) and pokemon2_can_fight:
            return (0,2)
        elif pokemon1_can_fight and not(pokemon2_can_fight):
            return (0,1)
        else:
            pokemon1 = self.__trainer1.get_pokemon_lst()[trainer1_pokemon_id]
            pokemon2 = self.__trainer2.get_pokemon_lst()[trainer2_pokemon_id]
            rounds_counter = 1
            while True:
                pokemon1.attack(pokemon2)
                self.__trainer1.change_pokemon_lst(pokemon1, trainer1_pokemon_id)
                self.__trainer2.change_pokemon_lst(pokemon2, trainer2_pokemon_id)

                pokemon1_can_fight = self.__trainer1.get_pokemon_lst()[trainer1_pokemon_id].can_fight()
                pokemon2_can_fight = self.__trainer2.get_pokemon_lst()[trainer2_pokemon_id].can_fight()
                if not(pokemon1_can_fight or pokemon2_can_fight):
                    return (rounds_counter, 0)
                elif not(pokemon1_can_fight) and pokemon2_can_fight:
                    return (rounds_counter, 2)
                elif pokemon1_can_fight and not(pokemon2_can_fight):
                    return (rounds_counter, 1)

                pokemon2.attack(pokemon1)
                self.__trainer1.change_pokemon_lst(pokemon1, trainer1_pokemon_id)
                self.__trainer2.change_pokemon_lst(pokemon2, trainer2_pokemon_id)

                pokemon1_can_fight = self.__trainer1.get_pokemon_lst()[trainer1_pokemon_id].can_fight()
                pokemon2_can_fight = self.__trainer2.get_pokemon_lst()[trainer2_pokemon_id].can_fight()
                if not(pokemon1_can_fight or pokemon2_can_fight):
                    return (rounds_counter, 0)
                elif not(pokemon1_can_fight) and pokemon2_can_fight:
                    return (rounds_counter, 2)
                elif pokemon1_can_fight and not(pokemon2_can_fight):
                    return (rounds_counter, 1)

                rounds_counter += 1




    def total_battle(self):
        '''
        This function when called will make the battle between two trainers.
        The Battle will be between all pokemons of each trainer until one of the trainers has no pokemons that can fight
         anymore - in that case the other trainer will be victorious. if both can't fight at the same time its a draw.
        :return: No returns, but prints the Trainer who won and the amount of rounds it took.
        '''
        fight_winner = 0
        index1 = -1
        index2 = -1
        round_counter = 0
        while True:
            if fight_winner == 0:
                index1 = Battle.available_to_fight(self.__trainer1.get_pokemon_lst())
                if index1 != -1:
                    index2 = Battle.most_damage_against(self.__trainer1.get_pokemon_lst()[index1], self.__trainer2.get_pokemon_lst())
                    if index2 != -1:
                        battle_res = self.dual_battle(index1, index2)
                        fight_winner = battle_res[1]
                        round_counter += battle_res[0]
                    else:
                        print("Trainer " + self.__trainer1.get_name() + " won the battle in " + str(round_counter) + " rounds")
                        break

                else:
                    index2 = Battle.available_to_fight(self.__trainer2.get_pokemon_lst())
                    if index2 == -1:
                        print("The battle ended with a draw")
                    else:
                        print("Trainer " + self.__trainer2.get_name() + "won the battle in " + str(round_counter) + " rounds")
                    break

            elif fight_winner == 1:
                index2 = Battle.most_damage_against(self.__trainer1.get_pokemon_lst()[index1], self.__trainer2.get_pokemon_lst())
                if index2 != -1:
                    battle_res = self.dual_battle(index1, index2)
                    fight_winner = battle_res[1]
                    round_counter += battle_res[0]
                else:
                    print("Trainer " + self.__trainer1.get_name() + " won the battle in " + str(round_counter) + " rounds")
                    break

            elif fight_winner == 2:
                index1 = Battle.most_damage_against(self.__trainer2.get_pokemon_lst()[index2], self.__trainer1.get_pokemon_lst())
                if index1 != -1:
                    battle_res = self.dual_battle(index1, index2)
                    fight_winner = battle_res[1]
                    round_counter += battle_res[0]
                else:
                    print("Trainer " + self.__trainer2.get_name() + "won the battle in " + str(round_counter) + " rounds")
                    break


    @staticmethod
    def available_to_fight(poke_lst):
        '''
        :param poke_lst: list of pokemons
        :return: return the index of the first pokemon available to fight, if none available returns -1
        '''
        for i, pokemon in enumerate(poke_lst):
            if pokemon.can_fight():
                return i
        return -1

    @staticmethod
    def most_damage_against(pokemon1, lst):
        '''
        :param pokemon: Pokemon type
        :param lst: list of pokemons
        :return: checking what pokemon will do the most amount of damage to the pokemon and return his index,
        :returns -1 of no pokemon is available to fight
        '''
        index = -1
        max_damage = 0
        for i, pokemon2 in enumerate(lst):
            dmg = pokemon2.get_damage(pokemon1)
            if pokemon2.can_fight() and max_damage < dmg:
                index = i
                max_damage = dmg
        return index












































