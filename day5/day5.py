from timeit import default_timer as timer


def input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    return data

def first(data):
    rules, numbers = data.split("\n\n")

    rule_pairs = []
    number_list = []

    total = 0



    for i in rules.splitlines():
        x, y = i.split("|")

        rule_pairs.append([int(x),int(y)])

    for i in numbers.splitlines():
        if i.strip():
            num = [int(x) for x in i.strip().split(",")]
            number_list.append(num)

    for nums in number_list:
        valid = True
        for rule in rule_pairs:

            if rule[0] in nums and rule[1] in nums:
                if nums.index(rule[0]) > nums.index(rule[1]):
                    valid = False

        if valid:
            if len(nums) % 2:
                total += nums[len(nums)//2]
            else:
                total += (nums[len(nums)//2 - 1] + nums[len(nums)//2]) / 2

    return total


def second(data):
    rules, numbers = data.split("\n\n")

    rule_pairs = []
    number_list = []

    total = 0



    for i in rules.splitlines():
        x, y = i.split("|")

        rule_pairs.append([int(x),int(y)])

    for i in numbers.splitlines():
        if i.strip():
            num = [int(x) for x in i.strip().split(",")]
            number_list.append(num)

    def build_graph(nums):
        graph = {num: set() for num in nums}
        for x, y in rule_pairs:
            if x in nums and y in nums:
                graph[x].add(y)
        return graph
    
    def topological_sort(graph):
        result = []
        visited = set()
        temp_visited = set()
        
        def visit(node):
            if node in temp_visited:
                return False
            if node in visited:
                return True
                
            temp_visited.add(node)
            
            for neighbor in graph[node]:
                if not visit(neighbor):
                    return False
                    
            temp_visited.remove(node)
            visited.add(node)
            result.insert(0, node)
            return True
            
        for node in graph:
            if node not in visited:
                if not visit(node):
                    return None
        return result
    
    for nums in number_list:
        valid = True
        for x, y in rule_pairs:
            if x in nums and y in nums:
                if nums.index(x) > nums.index(y):
                    valid = False
                    break
        
        if not valid:
            graph = build_graph(nums)
            sorted_nums = topological_sort(graph)
            if sorted_nums:
                mid = len(sorted_nums) // 2
                if len(sorted_nums) % 2 == 0:
                    total += (sorted_nums[mid-1] + sorted_nums[mid]) / 2
                else:
                    total += sorted_nums[mid]
    
    return int(total)


def main():
    data = input('input.txt')
    start = timer()
    print(first(data))
    end = timer()
    print(end-start)
    start = timer()
    print(second(data))
    end = timer()
    print(end-start)


if __name__ == "__main__":
    main()
