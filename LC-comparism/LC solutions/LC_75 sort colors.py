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


# -------------------- faster and smarter solution ---------------------
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, mid = 0
        right = len(nums)-1

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            
            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1