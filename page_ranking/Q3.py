import sys


# def read_input():
#     input_list = list()
#     try:
#         while True:
#             line = sys.stdin.readline().strip()
#             if not line:
#                 break
#             input_list.append(line.split(" "))
#     finally:
#         pass
#     return input_list

def main():
    input_data = sys.stdin.readlines()
    # input_data = read_input()

    # print(input_data)
    # print(len(input_data)) # test length

    for i in range(len(input_data)):
        input_data[i] = input_data[i].replace("\n\r", "")
        input_data[i] = input_data[i].replace("\r\n", "")
        input_data[i] = input_data[i].replace("\n", "")
        input_data[i] = input_data[i].replace("\r", "")
        input_data[i] = input_data[i].split(" ")

    # print(input_data) # test after deleting '\n' and split the numbers

    num_of_web_index = list()
    temp = 0

    # for i in range(len(input_data)):
    #     if len(input_data[i]) == 2:
    #         num_of_web_list.append(input_data[i][0])
    while temp < len(input_data):
        if len(input_data[temp]) == 2:
            num_of_web_index.append(temp)
            temp += (int(input_data[temp][0]) + 1)

    # print(num_of_web_index) # [0,9,15]
    # print(len(input_data)) # 19

    # Length of First block: 9-0-1
    # Second block: 15-9-1
    # Third block: 19-15-1

    num_of_blocks = len(num_of_web_index)  # =3

    for i in num_of_web_index:
        n = int(input_data[i][0])
        k = int(input_data[i][1])

        block = input_data[i + 1: i + n + 1]  # [['1', '3', '4', '5', '6'], ['0', '2', '3', '4', '5'], ['0', '1', '3',
        # '4', '5'], ['0', '2', '4', '5', '6'], [''], ['1', '6'], [''], ['0', '1', '3', '6']]
        # print(block)
        # print()

        # number_list = list(range(len(block)))
        count_list = [0] * len(block)

        for value in block:  # eg. value = ['1', '3', '4', '5', '6']
            if value[0] == '':
                continue
            for j in value:  # eg. j = '1'
                count_list[int(j)] += 1

        # print(count_list)  # eg. count_list[0] = [4, 2, 4, 4, 4, 4, 0, 4]

        index_dict = {}

        for i in range(len(count_list)):
            index_dict[i] = count_list[i]

        # print(index_dict)  # {0: 4, 1: 2, 2: 4, 3: 4, 4: 4, 5: 4, 6: 0, 7: 4}

        sort_arrangement = sorted(index_dict.items(), key=lambda x: (-x[1], x[0]))

        # print(sort_arrangement)

        node = sort_arrangement[k - 1]
        print(node[0])
        # print()

main()
