from timeit import default_timer as timer
import regex as re

def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

cube_dict = {
        'red': 12,
        'green':13,
        'blue':14,
        }


is_possible_game = 0
for line in read_input('input'):
    sets = line.split(';')
    game_index = int(re.findall(r'Game (\d+)',line)[0])
    correct_conditions = 1
    for set in sets:
        for color in cube_dict.keys():
            pattern = fr'(\d+) {color}'
            matches = re.findall(pattern,set)
            sum_of_matches = sum([int(x) for x in matches])
            if sum([int(x) for x in matches]) <= cube_dict[color]:
                correct_conditions *= 1
            else: 
                correct_conditions *= 0
    if correct_conditions == 1:
        is_possible_game += game_index


sum_all = 0
for line in read_input('input'):
    multiplication_max_value = 1
    for color in cube_dict.keys():
        pattern = fr'(\d+) {color}'
        max_value = max([int(x) for x in re.findall(pattern, line)])
        multiplication_max_value *= max_value
    sum_all += multiplication_max_value



if __name__ == "__main__":
    start = timer()
    print("The result to 1 is: {}".format(is_possible_game))
    end = timer()
    print(end - start)
    start = timer()
    print("The result to 2 is: {}".format(sum_all))
    end = timer()
    print(end - start)
