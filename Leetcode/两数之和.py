class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        location = []
        num1 = 0
        num2 = 0
        
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    num1 = i
                    num2 = j

        location.append(num1)
        location.append(num2)

        return location


test = Solution()
list1 = [2,7,11,15]
target = 9
print(test.twoSum(list1, target))