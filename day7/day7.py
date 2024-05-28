from timeit import default_timer as timer

def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.readlines()
    return data


data = read_input('input')

letter_map = { 'T': 'A', 'J': '!', 'Q': 'C', 'K': 'D', 'A': 'E' }

def score(hand):
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

def classify(hand):
    return max(map(score, replacement(hand)))

def replacement(hand):
    if hand == "":
        return [""]

    return [x + y
            for x in ("23456789TQKA" if hand[0] == "J" else hand[0]) 
            for y in replacement(hand[1:])
            ]


plays= []

for line in data:
    hand, bid = line.split()
    plays.append((hand, int(bid)))

total = 0

plays.sort(key = lambda play: strength(play[0]))
for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid





if __name__ == '__main__':
    start = timer()
    print(total)
    end = timer()
    print(end - start)
