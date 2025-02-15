from timeit import default_timer as timer


def input(filename):
    with open(filename, 'r') as f:
        input = f.read().splitlines()

    return input

def first(input):

    total = 0
    left = []
    right = []

    for line in input:
        l1, r1 = map(int, line.split())

        left.append(l1)
        right.append(r1)

    left.sort()
    right.sort()

    
    while left and right:
        l1 = left.pop(0)
        r1 = right.pop(0)

        total += abs(l1 - r1)
    return total


def second(input):

    total = 0
    left = []
    right = []

    for line in input:
        l1, r1 = map(int, line.split())

        left.append(l1)
        right.append(r1)

    left.sort()
    right.sort()

    for i in left:
        times = 0

        for x in right:
            if i == x:
                times += 1

        score = i * times
        total += score

    return total
    

if __name__ == "__main__":
    data = input('input.txt')
    start = timer()
    print(first(data))
    end = timer()
    print(end - start)
    start = timer()
    print(second(data))
    end = timer()
    print(end - start)
