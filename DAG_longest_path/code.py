def longest_path(order, order_list, path, size):
    path[order] = True
    for i in order_list[order]:
        i = int(i)
        if not path[i]:
            size = longest_path(i, order_list, path, size)
        size[order] = max([size[order], size[i] + 1])
    return size


def main():
    while True:
        order = int(input())
        order_list = list()

        if order == 0:
            break
        for i in range(order):
            #order_list[i] = input().strip().split()
            order_list.append(input().strip().split())

        size = len(order_list)
        pass_through = False
        print(longest_path(0, order_list, [pass_through] * size, [0] * size)[0])


main()
