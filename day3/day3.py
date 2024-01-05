def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().splitlines()
    return data
