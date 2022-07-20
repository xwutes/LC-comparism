# LC_209 Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        start,end = 0,0                             # 答案二分的比较上难度的题
        n = len(nums)
        ans = n + 1
        total = 0
        while end < n:
            total += nums[end]                      # 关键在于设定循环条件, 这里不控制<target的情况, 而是一直累加到>target
            while total >= target:                  # 然后这个位置再进行判断来形成这个窗口达到此条件之前
                ans = min(ans, end-start + 1)       # start是不动的,只有右指针end一直在后移
                total -= nums[start]                # 从这个位置再减掉原total中的数字
                start += 1
            end += 1                                # 解释了为何右指针在循环外这个事情
        
        return 0 if ans == n+1 else ans