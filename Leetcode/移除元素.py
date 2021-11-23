class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        temp = []

        for i in range(len(nums)):
            if (nums[i] == val):
                temp.append(i)
            else:
                count += 1
        
        for i in range(len(temp)):
            nums.remove(val)

        #print("temp", temp)        
        return count


test = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(test.removeElement(nums, val))
print(nums)