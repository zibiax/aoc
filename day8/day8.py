def read_input(read_name):
    input = []
    with open(f'{read_name}.txt', 'r') as f:
        for line in f:
            input.append(line.rstrip())
    return input

def follow_path(input_lines):

    instructions = input_lines[0]

    steps = 0

    mapping = dict()

    for i in range(2, len(input_lines)):
        split1 = input_lines[i].split('=')
        current = split1[0].strip()
        next_ele = split1[1].replace('(','').replace(')','').split(',')
        mapping[current] = (next_ele[0].strip(), next_ele[1].strip())
    current = 'AAA'

    while current != 'ZZZ':
        steps += 1
        direction = 0 if instructions[(steps-1)%len(instructions)] == 'L' else 1
        current = mapping[current][direction]
    return steps



if __name__ == "__main__":
    input_lines = read_input("input")
    print("Number of steps: ", follow_path(input_lines))
