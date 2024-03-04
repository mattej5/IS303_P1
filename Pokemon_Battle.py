# Authors: Vin Jones, Max Buhler, Jacob Boud, Parker Fellows

# Description: Group project expanding on the A7 assignment.
# Allows the user to choose 2 Pokemon to 'battle' until one faints

'''Required Libraries'''

import random

'''Required Classes'''

# same as A7
class Move:
    # creates the object 'Move'
    def __init__(self, move_name, elemental_type, low_attack_points, high_attack_points):
        self.move_name = move_name  # (string) the name of the move
        self.elemental_type = elemental_type    # (string) has a value like "Water", "Fire", "Grass", or "Normal"
        self.low_attack_points = low_attack_points  # (int) lowest value of points that can be generated for the move
        self.high_attack_points = high_attack_points    # (int) highest value of points that can be generated for the move

    # returns a string with the above variables, separated by a string, for the given move
    def get_info(self):
        message = f"{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points}-{self.high_attack_points} Attack Points"
        return message

    # returns an int of a randomly generated number between low_attack_points and high_attack_points of the move
    def generate_attack_value(self):
        low_attack_points = self.low_attack_points
        high_attack_points = self.high_attack_points
        attack_value = random.randint(low_attack_points,high_attack_points) # this line will use a function from the random library to produce a value between the upper and lower limits provided
        return attack_value

# defined by assignment A7 with some new methods
class Pokemon:
    # creates the object 'Pokemon'
    def __init__(self, name, elemental_type, hit_points, list_of_moves):
        self.name = name    # (string)
        self.elemental_type = elemental_type    # (string) will have a value of "Water", "Fire", or "Grass"
        self.hit_points = hit_points    # (int) represents the health of the pokemon
        self.list_of_moves = []     # list stores Move objects for each Pokemon object

    # returns a string with the name, elemental_type, and hit_points of the given pokemon
    def get_info(self):
        name = self.name
        elemental_type = self.elemental_type
        hit_points = self.hit_points
        message = f'{self.name} - Type: {self.elemental_type} - Hit Points: {self.hit_points}'
        return message

    # adds 15 points to hit_points and prints out a message with the new number of hit_points
    def heal(self):
        if self.hit_points <= 0:
            return None
        self.hit_points = self.hit_points + 15
        message = f"{self.name} has been healed to {self.hit_points} hit points."
        print(message)
        #return message
    
    # NEW used during pokemon_battle to display a number next to each pokemon as well as 'H: Heal 15 hit points"
    def display_choices(self):
        print("Your options:")
        for i, move in enumerate(self.list_of_moves):
            print(f'{i+1}: {move.get_info()}')
        print(f'H: Heal 15 hit points')

    # NEW used during pokemon_battle to call the generate_attack_value and uses any valid multipliers
    def attack(self, move_index, opponent_pokemon):
        if self.hit_points <= 0:
            return None
        print(f'\n{self.name} used {self.list_of_moves[move_index].move_name}!')
        hit_points_lost = self.list_of_moves[move_index].generate_attack_value()
        if self.list_of_moves[move_index].elemental_type == "Normal":
            pass
        elif self.list_of_moves[move_index].elemental_type == "Grass" and opponent_pokemon.elemental_type == "Fire":
            hit_points_lost = hit_points_lost * 0.5
            print("It's not very effective...")
        elif self.list_of_moves[move_index].elemental_type == "Grass" and opponent_pokemon.elemental_type == "Water":
            hit_points_lost = hit_points_lost * 2.0
            print(f"Its super effective!")
        elif self.list_of_moves[move_index].elemental_type == "Fire" and opponent_pokemon.elemental_type == "Water":
            hit_points_lost = hit_points_lost * 0.5
            print("It's not very effective...")
        elif self.list_of_moves[move_index].elemental_type == "Fire" and opponent_pokemon.elemental_type == "Grass":
            hit_points_lost = hit_points_lost * 2.0
            print("It's super effective!")
        elif self.list_of_moves[move_index].elemental_type == "Water" and opponent_pokemon.elemental_type == "Grass":
            hit_points_lost *= 0.5
            print(f"It's not very effective...")
        elif self.list_of_moves[move_index].elemental_type == "Water" and opponent_pokemon.elemental_type == "Fire":
            hit_points_lost *= 2.0
            print(f"It's super effective!")

        critical_hit = random.randint(1,100)

        if critical_hit < 7:
            hit_points_lost = hit_points_lost * 1.5
            print("Critical hit!")

        hit_points_lost = int(round(hit_points_lost,0))
        opponent_pokemon.hit_points = opponent_pokemon.hit_points - hit_points_lost
        print(f"{opponent_pokemon.name} took {hit_points_lost} points of damage!")
        input("\nPress enter to proceed...\n")

'''Required Functions'''
    
# NEW Starts the battle between chosen Pokemon and opponent pokemon, continues until HP = 0
def pokemon_battle(your_pokemon, opponent_pokemon):
    # this function continues until your_pokemon OR opponent_pokemon is defeated
    print("BATTLE START!")
    print(f"{opponent_pokemon.name} wants to fight!")
    print(f'Go! {your_pokemon.name}!\n')
   
    while your_pokemon.hit_points > 0 and opponent_pokemon.hit_points > 0:
        print(f'Opponent: {opponent_pokemon.get_info()}')
        print(f'You: {your_pokemon.get_info()}\n')

        your_pokemon.display_choices()
        player_input = input('Choose an option: ')

        if player_input.upper() == "H":
            your_pokemon.heal()
        elif (int(player_input) == 1 or int(player_input) == 2):
            player_input = int(player_input)
            your_pokemon.attack(player_input - 1, opponent_pokemon)

        cpu_input = random.randint(1,3)

        if cpu_input == 3:
            opponent_pokemon.heal()
        elif (int(cpu_input) == 1 or int(cpu_input) == 2):
            cpu_input = int(cpu_input)
            opponent_pokemon.attack(cpu_input - 1, your_pokemon)

    if your_pokemon.hit_points <= 0:
        print(f'{your_pokemon.name} has been defeated.')
        print(f'{opponent_pokemon.name} has won!')
    elif opponent_pokemon.hit_points <= 0:
        print(f'{opponent_pokemon.name} has been defeated.')
        print(f'{your_pokemon.name} has won!')
        
'''Logical Flow starts here'''

# Part 1: Creating Move objects

# creates 9 'Move' objects and stores them in a list
Tackle = Move('Tackle','Normal',5,20)
Quick_Attack = Move('Quick Attack','Normal',6,25)
Slash = Move('Slash','Normal',10,30)
Flamethrower = Move('Flamethrower','Fire',5,30)
Ember = Move('Ember','Fire',10,20)
Water_Gun = Move('Water Gun','Water',5,15)
Hydro_Pump = Move('Hydro Pump','Water',20,25)
Vine_Whip = Move('Vine Whip','Grass',10,25)
Solar_Beam = Move('Solar Beam','Grass',18,27)

Move_Names = [Tackle, Quick_Attack, Slash, Flamethrower, Ember, Water_Gun, Hydro_Pump, Vine_Whip, Solar_Beam]
print(f'These are the moves the pokemon will randomly select from:')
for move in Move_Names:
    print(f'\t{move.get_info()}')
print()

# Part 2: Creating Pokemon objects and assigning moves

# creates 3 'Pokemon' objects and stores them in a list
Bulbasaur = Pokemon('Bulbasaur','Grass',60,[])
Charmander = Pokemon('Charmander','Fire',55,[])
Squirtle = Pokemon('Squirtle','Water',65,[])

Pokemon_Names = [Bulbasaur, Charmander, Squirtle]    

for pokemon in Pokemon_Names:
    possible_moves = []
    for move in Move_Names:
        if move.elemental_type == pokemon.elemental_type or move.elemental_type == 'Normal':
            possible_moves.append(move)
    assignedmoves = random.sample(possible_moves, 2)
    for assignedmove in assignedmoves:
        Move_Names.remove(assignedmove)
    pokemon.list_of_moves = assignedmoves
    
for pokemon in Pokemon_Names:
    print(f"{pokemon.name} was assigned:")
    for move in pokemon.list_of_moves:
        print(f'\t{move.get_info()}')
print()

# Part 3: Choosing your Pokemon and the Opponent's Pokemon

print("Available Pokemon:")
for i, pokemon in enumerate(Pokemon_Names):
    print(f'{i+1}: {pokemon.get_info()}')
    
your_pokemon_choice = int(input("Choose the # of your pokemon: "))

for i, pokemon in enumerate(Pokemon_Names):
    if (i+1) == your_pokemon_choice:
        your_pokemon = pokemon
        Pokemon_Names.remove(Pokemon_Names[i])

print(f'\nYou chose {your_pokemon.name} as your pokemon\n')

for i, pokemon in enumerate(Pokemon_Names):
    print(f'{i+1}: {pokemon.get_info()}')

opponent_pokemon_choice = int(input("Choose the # of the opponent pokemon: "))

for i, pokemon in enumerate(Pokemon_Names):
    if (i+1) == opponent_pokemon_choice:
        opponent_pokemon = pokemon
        Pokemon_Names.remove(Pokemon_Names[i])

print(f'\nYou chose {opponent_pokemon.name} as the opponent.\n')
# Part 4: Battle!

pokemon_battle(your_pokemon, opponent_pokemon)