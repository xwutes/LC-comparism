#LC_75 sort colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ptrhead = 0

        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptrhead] = nums[ptrhead],nums[i]
                ptrhead += 1

        for i in range(ptrhead, n):
            if nums[i] == 1:
                nums[i], nums[ptrhead] = nums[ptrhead],nums[i]
                ptrhead += 1