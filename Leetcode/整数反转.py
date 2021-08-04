import math

# x = 123
# str_x = str(x)
# length = len(str_x)

# result = 0

# for i in range(length):
#     result += int(str_x[-(i+1)]) * math.pow(10, length - 1)
#     length -= 1

# print(int(result))

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        str_x = str(x)
        if str_x[0] == '-':
            result = str_x[0] + str_x[-1:-len(str_x):-1]
        else:
            result = str_x[::-1]

        if -2**31 <= int(result) <= 2**31 - 1:
            return int(result)
        else:
            return 0

test = Solution()
x = 1534236469
print(test.reverse(x))