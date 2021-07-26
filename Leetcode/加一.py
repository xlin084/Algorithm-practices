class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # digits[-1] += 1

        length = len(digits)
        for i in range(-1, -length-1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits


test = Solution()
digits = [9]
print(test.plusOne(digits))