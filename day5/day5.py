from timeit import default_timer as timer


def input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    return data

def first(data):
    pass


def main():
    data = input('input.txt')
    start = timer()
    print(first(data))
    end = timer()
    print(end-start)


if __name__ == "__main__":
    main()
