from timeit import default_timer as timer

def read_input(input):
    with open(f'{input}.txt', 'r') as f:
        data = f.read().splitlines()
    return data

input_list = read_input('input')
cur_num = []
sum = 0
for y in range(0, len(input_list)):
    for x in range(0, len(input_list[0])):
        if input_list[y][x].isnumeric():
            cur_num.append(input_list[y][x])
        
        if not input_list[y][x].isnumeric() or x == (len(input_list[0])-1):
            length = len(cur_num)
            if length > 0:
                x_start = max(0, x-length-1)
                x_end = min(len(input_list[0])-1, x)
                y_start = max(0, y-1)
                y_end = min(len(input_list)-1, y+1)

                flag = False
                for xx in range(x_start, x_end+1):
                    for yy in range(y_start, y_end+1):
                        if (input_list[yy][xx] != '.' and 
                            not input_list[yy][xx].isnumeric()):
                            sum += int("".join(cur_num))
                            cur_num = []
                            flag = True
                            break
                    if flag:
                        break
                cur_num = []

if __name__ == "__main__":
    start = timer()
    print("The result to 1 is: {}".format(sum))
    end = timer()
