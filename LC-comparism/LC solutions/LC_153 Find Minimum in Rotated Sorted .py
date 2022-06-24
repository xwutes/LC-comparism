# LC_153 Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1
        
        
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])             # compairing value with left most
                break
            
            mid = (l + r)//2
            res = min(res, nums[mid])               # compairing value with middle(standard approch for BS)
            if nums[l] <= nums[mid]:
                # res = min(res, nums[mid])         # this is falt position  
                l = mid + 1
            else:
                r = mid - 1                         # [2,1],1 and [4,5,6,7,0,1,2],0 and [3,1,2],1
        return res