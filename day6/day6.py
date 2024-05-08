from timeit import default_timer as timer
# from collections import defaultdict


def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().strip()
    return data

score = 0

data = read_input('input')

time, distance = data.split("\n")
time = time.split(":")[1].split()
distance = distance.split(":")[1].split()
print(time)
print(distance)
