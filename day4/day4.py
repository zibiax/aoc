from timeit import default_timer as timer

def input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    return data

def first(data, pattern):

    ans = 0

    lines = data.split('\n')
    rows, cols = len(lines), len(lines[0])

    pattern_len = len(pattern)

    for line in lines:
        for i in range(cols - pattern_len + 1):
            if line[i:i+pattern_len] == pattern:
                ans += 1
            if line[i:i+pattern_len][::-1] == pattern:
                ans += 1

    for j in range(cols):
        for i in range(rows - pattern_len + 1):
            vertical = ''.join(lines[i + k][j] for k in range(pattern_len))
            if vertical == pattern:
                ans += 1
            if vertical[::-1] == pattern:
                ans += 1
                
    for i in range(rows - pattern_len + 1):
        for j in range(cols - pattern_len + 1):
            diagonal = ''.join(lines[i + k][j + k] for k in range(pattern_len))
            if diagonal == pattern:
                ans += 1
            if diagonal[::-1] == pattern:
                ans += 1
                
    for i in range(rows - pattern_len + 1):
        for j in range(pattern_len - 1, cols):
            diagonal = ''.join(lines[i + k][j - k] for k in range(pattern_len))
            if diagonal == pattern:
                ans += 1
            if diagonal[::-1] == pattern:
                ans += 1
    


    return ans

def second(data, pattern):

    ans = 0

    lines = data.split('\n')
    rows, cols = len(lines), len(lines[0])


    for i in range(rows-2):
       for j in range(cols-2):
           top_left = lines[i][j]
           middle = lines[i+1][j+1]
           bottom_right = lines[i+2][j+2]
           bottom_left = lines[i+2][j]
           top_right = lines[i][j+2]
           
           if middle == 'A':
               patterns = [
                   (top_left == 'M' and bottom_right == 'S' and 
                    bottom_left == 'M' and top_right == 'S'),
                   (top_left == 'M' and bottom_right == 'S' and 
                    bottom_left == 'S' and top_right == 'M'),
                   (top_left == 'S' and bottom_right == 'M' and 
                    bottom_left == 'M' and top_right == 'S'),
                   (top_left == 'S' and bottom_right == 'M' and 
                    bottom_left == 'S' and top_right == 'M')
               ]
               ans += sum(1 for p in patterns if p)
               
    return ans



def main():
    data = input('input.txt')
    start = timer()
    print(first(data, 'xmas'))
    end = timer()
    print(end-start)
    start = timer()
    print(second(data, 'mas'))
    end = timer()
    print(end-start)


if __name__ == "__main__":
    main()
