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

sum2 = 0

for y in range(0, len(input_list)):
    for x in range(0, len(input_list[0])):
        nums = []
        if input_list[y][x] == '*':
            length = 1
            x_start = max(0, x-length)
            x_end = min(len(input_list[0])-1, x+1)
            y_start = max(0, y-1)
            y_end = min(len(input_list)-1, y+1)

            considered = []
            for xx in range(x_start, x_end+1):
                for yy in range(y_start, y_end+1):
                    if input_list[yy][xx].isnumeric() and [xx, yy] not in considered:
                        x2 = xx
                        cur_num = []
                        while True:
                            x2 -= 1
                            if x2>=0:
                                if not input_list[yy][x2].isnumeric():
                                    break
                            else:
                                break
                        x2+=1
                        while True:
                            if x2 < len(input_list[0]):
                                if input_list[yy][x2].isnumeric():
                                    considered.append([x2, yy])
                                    cur_num.append(input_list[yy][x2])
                                    x2+=1
                                else:
                                    break
                            else:
                                break
                        nums.append(int("".join(cur_num)))
            if len(nums) == 2:
                sum2 += nums[0]*nums[1]
print(sum)

if __name__ == "__main__":
    start = timer()
    print("The result to 1 is: {}".format(sum))
    end = timer()
    print(end - start)
    start = timer()
    print("The result to 2 is: {}".format(sum2))
    end = timer()
    print(end - start)
