from timeit import default_timer as timer
from collections import defaultdict
def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().strip()
    return data

score = 0
score2 = 0
input = read_input('input')

lines = input.split("\n")

D = defaultdict(int)

for i, line in enumerate(lines):
    D[i] += 1
    first, second = line.split("|")
    id, card = first.split(":")
    card_nums = [int(x) for x in card.split()]
    second_nums = [int(x) for x in second.split()]
    val = len(set(card_nums) & set(second_nums))
    if val > 0:
        score +=  2**(val - 1)
    for j in range(val):
        D[i + 1 + j] += D[i]
    
    score2 = sum(D.values())


if __name__ == "__main__":
    start = timer()
    print("The result to 1 is: {}".format(score))
    end = timer()
    print(end - start)
    start = timer()
    print("The result to 2 is: {}".format(score2))
    end = timer()
    print(end - start)
