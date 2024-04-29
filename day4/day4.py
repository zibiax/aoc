from timeit import default_timer as timer

def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

def sum(data):


if __name__ == "__main__":
    start = timer()
    print("The result to 1 is: {}".format(sum))
    end = timer()
    print(end - start)
'''    start = timer()
    print("The result to 2 is: {}".format(sum2))
    end = timer()
    print(end - start)'''
