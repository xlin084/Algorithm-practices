# list1 = [1,2,3,4,5,6,7]
# # print(list1[len(list1) -3 : len(list1)])
# k = 3
# # temp_list = list1[len(list1) -3 : len(list1)] + list1[0:len(list1) -3]
# temp_list = list1[len(list1) -3 : len(list1)]
# del list1[len(list1) -3 : len(list1)] # method 3
# list1 = temp_list + list1
# print(list1)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k : len(nums)] + nums[0:len(nums) - k]  # method 1
        # n = len(nums) # method 2
        # k %= n
        # nums[:] = nums[-k:] + nums[:-k]
        return nums

test = Solution()
list1 = [1,2]
k = 5
result = test.rotate(list1, k)
print(result)