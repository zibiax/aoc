from timeit import default_timer as timer
from collections import defaultdict


def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().strip()
    return data

score = 0

data = read_input('input')
seed, *blocks = data.split("\n\n")

seeds = list(map(int, seed.split(":")[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    new = []

    for x in seeds:
        for a, b, c in ranges:
            if b <= x < b + c:
                new.append(x - b + a)
                break
        
        else:
            new.append(x)
    seeds = new

score = min(seeds)

if __name__ == "__main__":
    start = timer()
    print("The result to 1 is: {}".format(score))
    end = timer()
    print(end - start)
'''    start = timer()
    print("The result to 2 is: {}".format(score2))
    end = timer()
    print(end - start)'''
