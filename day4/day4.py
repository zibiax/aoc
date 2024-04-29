from timeit import default_timer as timer

def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().strip()
    return data

score = 0

input = read_input('input')

lines = input.split("\n")

for line in lines:
    first, second = line.split("|")
    id, card = first.split(":")
    card_nums = [int(x) for x in card.split()]
    second_nums = [int(x) for x in second.split()]
    val = len(set(card_nums) & set(second_nums))
    if val > 0:
        score +=  2**(val - 1)

if __name__ == "__main__":
    start = timer()
    print("The result to 1 is: {}".format(score))
    end = timer()
'''
    print(end - start)
    start = timer()
    print("The result to 2 is: {}".format(sum2))
    end = timer()
    print(end - start)'''
