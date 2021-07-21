class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i-1]:
                del nums[i]

        return nums


test = Solution()
nums = [1,1,2]
new_list = test.removeDuplicates(nums)
print(len(new_list))
print(new_list)

    