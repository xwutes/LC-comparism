#LC_11 Container With Most Water maxArea

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        maxA = 0
        
        while i<j:
            area = min(height[i],height[j]) * (j-i)
            maxA = max(maxA, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxA