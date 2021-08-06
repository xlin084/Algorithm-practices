# s = "loveleetcode"
# for i in range(len(s)):
#     if s.find(s[i]) == s.rfind(s[i]):
#         print(i)
#         break
#     print(0)

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # first way: 
        # for i in range(len(s)):
        #     if s.find(s[i]) == s.rfind(s[i]):
        #         return i
        # return -1

        # second way:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return s.index(s[i])


test = Solution()
s = 'leetcode'
print(test.firstUniqChar(s))
# test.firstUniqChar(s)