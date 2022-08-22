
from random import shuffle

points = [1,2,3,4,5,8,10]
letter_value_groups = [['E', 'A', 'I', 'O','N', 'R', 'T', 'L', 'S', 'U'], ['D', 'G'], ['B', 'C', 'M', 'P'], ['F', 'H', 'V', 'W', 'Y'], ['K'], ['J', 'X'], ['Q', 'Z']]
number_of_tiles = [12,9,8,6,4,3,2,1]
letter_distribution_groups = [['E'], ['A','I'], ['O'], ['N','R','T'], ['L','S','U','D'], ['G'], ['B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y'], ['K', 'J', 'X', 'Q', 'Z']]


def letters_to_points(letter_value_groups):
    letters_to_points = {}

    for letters in range(len(letter_value_groups)):
        for letter in letter_value_groups[letters]:
            letters_to_points[letter] = points[letters]

    return letters_to_points

def get_letter_distribution(letter_distributions_groups):
    letter_distribution = {}

    for letters in range(len(letter_distributions_groups)):
        for letter in letter_distribution_groups[letters]:
            letter_distribution[letter] = number_of_tiles[letters]
        
    return letter_distribution


def calculate_word_score(input_word, letter_scores):

    score = 0
    formatted_word = input_word.strip().upper()
    for letter in formatted_word:
        score += [value for key,value in letter_scores.items() if key == letter][0]

    return score


def generate_bag(letter_distribution):

    bag = []
    for key, value in letter_distribution.items():
        letter_tiles = [*key*value]
        bag.append(letter_tiles)

    return sum(bag,[])

def deal_tiles(bag):
    
    player_hand = []
    while len(player_hand)<=8:
        player_hand.append(bag.pop())
    
    return player_hand


# Task 1
letter_values = letters_to_points(letter_value_groups)
guardian_score = calculate_word_score('GUARDIAN', letter_values)

# Task 2 & 3

letter_distribution = get_letter_distribution(letter_distribution_groups)
bag = generate_bag(letter_distribution)
shuffle(bag)
player_hand = deal_tiles(bag)
print("\n Your Hand is:")
print(* player_hand, sep=', ')
