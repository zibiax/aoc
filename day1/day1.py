def input(filename):
    with open(filename, 'r') as f:
        input = f.read().splitlines()

    return input

def first(input):

    total = 0
    l = []
    r = []

    for line in input:
        left, right = map(int, line.split())

        l.append(left)
        r.append(right)

    l.sort()
    r.sort()

    
    while l and r:
        left = l.pop(0)
        right = r.pop(0)

        total += abs(left - right)
    return total

if __name__ == "__main__":
    data = input('input.txt')
    print(first(data))
