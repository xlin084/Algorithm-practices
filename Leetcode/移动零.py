class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.sort()

        #         index = 0 # 非0的index
        #         for i in range(len(nums)):
        #             if nums[i] != 0:
        #                 index = i
        #                 break
            
        #         del nums[0:index]

        #         for i in range(index):
        #             nums.append(0)

        #         return nums
            
        # return nums

        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[index]
                nums[index] = nums[i]
                nums[i] = temp
                index += 1
        return nums


test = Solution()
input = [0,1,0,3,12]
# input = [2,1]
# input = [1,0,1]
print(test.moveZeroes(input))