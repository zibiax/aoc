from timeit import default_timer as timer

def input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    return data

def first(data, pattern):

    times = 0

    lines = data.split('\n')
    rows, cols = len(lines), len(lines[0])

    pattern_len = len(pattern)

    for line in lines:
        for i in range(cols - pattern_len + 1):
            if line[i:i+pattern_len] == pattern:
                times += 1
            if line[i:i+pattern_len][::-1] == pattern:
                times += 1

    for j in range(cols):
        for i in range(rows - pattern_len + 1):
            vertical = ''.join(lines[i + k][j] for k in range(pattern_len))
            if vertical == pattern:
                times += 1
            if vertical[::-1] == pattern:  # backwards
                times += 1
                
    for i in range(rows - pattern_len + 1):
        for j in range(cols - pattern_len + 1):
            diagonal = ''.join(lines[i + k][j + k] for k in range(pattern_len))
            if diagonal == pattern:
                times += 1
            if diagonal[::-1] == pattern:  # backwards
                times += 1
                
    for i in range(rows - pattern_len + 1):
        for j in range(pattern_len - 1, cols):
            diagonal = ''.join(lines[i + k][j - k] for k in range(pattern_len))
            if diagonal == pattern:
                times += 1
            if diagonal[::-1] == pattern:  # backwards
                times += 1
    


    return times


def main():
    data = input('input.txt')

    print(first(data, 'XMAS'))


if __name__ == "__main__":
    main()
