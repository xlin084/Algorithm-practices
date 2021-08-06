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
        for i in range(len(s)):
            if s.find(s[i]) == s.rfind(s[i]):
                return i
        return -1


test = Solution()
s = 'loveleetcode'
print(test.firstUniqChar(s))