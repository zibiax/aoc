import re as r
from timeit import default_timer as timer

def input(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def first(data):

    filter = r.findall(r'mul\(\d+,\d+\)', data)
    product = 0

    for i in filter:
        num1, num2 = map(int, i[4:-1].split(','))
        score = num1 * num2
        product += score
    return product

def second(data):
    product = 0
    enabled = True
    
    for match in r.finditer(r'(?:do\(\)|don\'t\(\)|mul\(\d+,\d+\))', data):
        cmd = match.group()
        if cmd == 'do()':
            enabled = True
        elif cmd == "don't()":
            enabled = False
        elif enabled and cmd.startswith('mul'):
            nums = cmd[4:-1].split(',')
            product += int(nums[0]) * int(nums[1])
            
    return product

def main():
    data = input('input.txt')
    start = timer()
    print(first(data))
    end = timer()
    print(end - start)
    start = timer()
    print(second(data))
    end = timer()
    print(end - start)
        

if __name__ == "__main__":
    main()
