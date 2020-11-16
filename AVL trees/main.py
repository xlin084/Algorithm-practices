import sys


class Node:  # create a node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def create_tree(self, list1):
        temp_list = list()
        # row = list1[self.data]
        index = self.data
        for i in range(len(list1[index])):
            if list1[index][i] == '1':
                temp_list.append(i)

        if len(temp_list) == 1:
            self.left = Node(temp_list[0])
            self.left.create_tree(list1)
        elif len(temp_list) == 2:
            self.left = Node(temp_list[0])
            self.right = Node(temp_list[1])
            self.left.create_tree(list1)
            self.right.create_tree(list1)


def height(root):
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1


def is_balanced(root):
    if root is None:
        return True

    lh = height(root.left)  # left height
    rh = height(root.right)  # right height

    # if (abs(lh - rh) == 1 or abs(lh - rh) == 0 or abs(lh - rh) == -1) and is_balanced(
    #         root.left) is True and is_balanced(
    #         root.right) is True:
    #     return True

    if abs(lh - rh) < 2:
        if is_balanced(root.left) is True and is_balanced(root.right) is True:
            return True

    return False


# row = int(input())
# root = int(input())

input_data = sys.stdin.readlines()

# print(input_data)

# for i in input_data:
#     data = data.replace("\n", "")

for i in range(len(input_data)):
    input_data[i] = input_data[i].replace("\n", "")
    input_data[i] = input_data[i].split(" ")

    # print(input_data)

deter_list = list()
temp = 0

while temp < len(input_data):
    if len(input_data[temp]) == 2:
        deter_list.append(temp)
        temp += (int(input_data[temp][0]) + 1)
        # print(temp)

for i in deter_list:  # [0][6]...
    number_of_row = int(input_data[i][0])
    root = int(input_data[i][1])
    local_root = Node(root)

    matrix_list = input_data[i + 1: i + number_of_row + 1]
    local_root.create_tree(matrix_list)

    # print(height(local_root), is_balanced(local_root))
    print(f"{height(local_root)} {is_balanced(local_root)}")
