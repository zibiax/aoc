from timeit import default_timer as timer

def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.readlines()
    return data


data = read_input('input')

letter_map = { 'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E' }

def classify(hand):
    counts = [hand.count(card) for card in hand]
    
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


def strength(hand):
    return (classify(hand), [letter_map.get(card, card) for card in hand])


plays= []

for line in data:
    hand, bid = line.split()
    plays.append((hand, int(bid)))

total = 0

plays.sort(key = lambda play: strength(play[0]))
for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid

    
print(total)

if __name__ == '__main__':
    start = timer()
    print(total)
    end = timer()
    print(end - start)
