class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_num = sorted(list(set(nums)))
        len_unique_num = len(unique_num)
        for i in range(len_unique_num):
            nums[i] = unique_num[i]
        return len_unique_num

        