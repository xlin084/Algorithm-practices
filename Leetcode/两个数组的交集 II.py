class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []

        for i in range(len(nums1)):
            index = nums1[i]
            for j in range(len(nums2)):
                if index == nums2[j]:
                    result.append(nums2[j])
                    # nums2.pop(nums2[j])
                    nums2.pop(j)
                    break
        return result


test = Solution()
list1 = [4,9,5]
list2 = [9,4,9,8,4]
print(test.intersect(list1, list2))