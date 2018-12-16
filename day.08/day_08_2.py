class Node:
    def __init__(self):
        self.children = []
        self.meta = []

class Nums:
    def __init__(self, line):
        self.current = 0
        self.nums = [int(x) for x in line.split(' ')]
    
    def next(self):
        result = self.nums[self.current]
        self.current = min(self.current + 1, len(self.nums) - 1)
        return result

def create_node(nums):
    result = Node()

    total_children = nums.next()
    total_meta = nums.next()

    for i in range(0, total_children):
        result.children.append(create_node(nums))
    for i in range(0, total_meta):
        result.meta.append(nums.next())

    return result

def sum_all_meta(current_node):
    result = sum(current_node.meta)

    for c in current_node.children:
        result += sum_all_meta(c)

    return result

# seems like there's opportunity for dynamic programming here
def sum_node_value(current_node):
    if len(current_node.children) == 0:
        return sum(current_node.meta)
    
    result = 0
    for m in current_node.meta:
        m_corrected = m - 1
        if m_corrected < 0 or m_corrected >= len(current_node.children):
            continue
        result += sum_node_value(current_node.children[m_corrected])
    return result

def main():
    nums = Nums(input())
    root = create_node(nums)
    # print(sum_all_meta(root))
    print(sum_node_value(root))

main()
