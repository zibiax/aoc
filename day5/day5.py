from timeit import default_timer as timer
from collections import defaultdict


def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().strip()
    return data

score = 0

data = read_input('input')

inputs, *blocks = data.split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    new = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break       
        else:
            new.append((s, e))
    seeds = new

score2 = min(seeds)[0]

seed, *block = data.split("\n\n")

seed = list(map(int, seed.split(":")[1].split()))

for blo in block:
    rang = []
    for line in blo.splitlines()[1:]:
        rang.append(list(map(int, line.split())))
    new = []
    for x in seed:
        for a, b, c in rang:
            if b <= x < b + c:
                new.append(x - b + a)
                break
        else:
            new.append(x)

    seed = new
print(seed)
score = min(seed)
print(score)
'''
if __name__ == "__main__":
    start = timer()
    print("The result to 1 is: {}".format(score))
    end = timer()
    print(end - start)
    start = timer()
    print("The result to 2 is: {}".format(score2))
    end = timer()
    print(end - start)'''
