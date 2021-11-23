class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1, 2, -1):
            if (nums[i] == nums [i-1] and nums[i-1] == nums[i-2]):
                del nums[i]

        return nums


test = Solution()
nums = [0,0,1,1,1,1,2,3,3]
new_list = test.removeDuplicates(nums)
print(len(new_list))
print(new_list)

