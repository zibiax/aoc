from timeit import default_timer as timer
# from collections import defaultdict


def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().strip()
    return data

score = 0

data = read_input('input')

time, distance = data.split("\n")
time = time.split(":")[1].split()
distance = distance.split(":")[1].split()


def calculate_ways(time, distance):
    counter = 0
    for i in range(1, time + 1):
        speed = i
        rt = time - i
        td = rt * speed
        if td >= distance:
            counter += 1
    return counter




if __name__ == "__main__":
    start = timer()
    total_counter = 1
    for i in range(len(time)):
        counter = calculate_ways(int(time[i]), int(distance[i]))
        total_counter *= counter
    total_counter -= 1
    print(total_counter)
    end = timer()
    print(end - start)
    
    # part 2

    time, distance = data.split("\n")
    time = time.split(":")[1].replace(" ", "")
    distance = distance.split(":")[1].replace(" ", "")
    start = timer()
    print(calculate_ways(int(time), int(distance)))
    end = timer()
    print(end - start)

 
