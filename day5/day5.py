from timeit import default_timer as timer


def input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    return data

def first(data):
    rules, numbers = data.split("\n\n")

    rule_pair = []
    number_list = []

    total = 0



    for i in rules.splitlines():
        x, y = i.split("|")

        rule_pair.append([int(x),int(y)])

    for i in numbers.splitlines():
        if i.strip():
            num = [int(x) for x in i.strip().split(",")]
            number_list.append(num)

    for nums in number_list:
        valid = True
        for rule in rule_pair:

            if rule[0] in nums and rule[1] in nums:
                if nums.index(rule[0]) > nums.index(rule[1]):
                    valid = False

        if valid:
            if len(nums) % 2:
                total += nums[len(nums)//2]
            else:
                total += (nums[len(nums)//2 - 1] + nums[len(nums)//2]) / 2

    return total

def main():
    data = input('input.txt')
    start = timer()
    print(first(data))
    end = timer()
    print(end-start)


if __name__ == "__main__":
    main()
