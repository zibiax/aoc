from timeit import default_timer as timer

def input_data(filename):
    with open(filename, 'r') as f:
        input = f.read().splitlines()

    return input

def first(data):

    safe = 0

    for line in data:

        is_increasing = None
        is_safe = True
        line = list(map(int, line.split()))

        for i in range(len(line) - 1):
            diff = line[i+1] - line[i]

            if abs(diff) > 3 or abs(diff) == 0:
                is_safe = False
                break

            if is_increasing is None and diff != 0:
                is_increasing = diff > 0

            elif diff != 0:
                if (is_increasing and diff < 0) or (not is_increasing and diff > 0):
                    is_safe = False
                    break
        if is_safe:
            safe += 1

    return safe

def second(data):

    safe = 0

    for line in data:

        line = list(map(int, line.split()))

        is_safe = check_line(line)



        if not is_safe:

            for j in range(len(line)):
                test_line = line[:j] + line[j+1:]
                if check_line(test_line):
                    is_safe = True
                    break




        if is_safe:
            safe += 1

    return safe

def check_line(line):

    is_increasing = None
    is_safe = True

    for i in range(len(line) - 1):

        diff = line[i+1] - line[i]

        if abs(diff) > 3 or abs(diff) == 0:
            is_safe = False
            break

        if is_increasing is None and diff != 0:
            is_increasing = diff > 0

        elif diff != 0:
            if (is_increasing and diff < 0) or (not is_increasing and diff > 0):
                is_safe = False
                break
    return is_safe

def main():
    data = input_data('input.txt')
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
