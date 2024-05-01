from timeit import default_timer as timer
from collections import defaultdict
def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().strip()
    return data

score = 0


if __name__ == "__main__":
    start = timer()
    print("The result to 1 is: {}".format(score))
    end = timer()
    print(end - start)
'''    start = timer()
    print("The result to 2 is: {}".format(score2))
    end = timer()
    print(end - start)'''
