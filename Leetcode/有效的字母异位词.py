# s = "anagram" 
# t = "nagaram"

# temp_a = sorted(s)
# temp_b = sorted(t)

# print(temp_a == temp_b)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        
        temp_a = sorted(s)
        temp_b = sorted(t)

        return temp_a == temp_b


test = Solution()
s = "anagram" 
t = "nagaram"
print(test.isAnagram(s, t))