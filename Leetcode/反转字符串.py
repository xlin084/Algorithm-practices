# temp = ["h","e","l","l","o"]
# left = 0
# right = len(temp) - 1

# while (left < right):
#     temp[left], temp[right] = temp[right], temp[left]
#     left += 1
#     right -= 1

# print(temp)
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while (left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s            


test = Solution()
string = ["h","e","l","l","o"]
print(test.reverseString(string))