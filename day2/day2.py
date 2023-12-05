def read_input(text):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().splitlines()
    return data
