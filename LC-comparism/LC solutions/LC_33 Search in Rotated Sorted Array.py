# LC_33 Search in Rotated Sorted Array

def search(nums, target):
    if not nums or len(nums) == 0:                     # edge case for considering empty input
        return -1
    left = 0
    right = len(nums) - 1
    while left + 1 < right:                            # about the two pointer starting point(this will overcome the fault of[1,2,2,4,5,5])
        mid = (left + right) // 2                      # if mid value is 3.5 then here will assign 3
        # mid = left +(left - right) // 2
        if nums[mid] == target:
            return mid                                 # edge case of target in mid index
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target and target <= nums[mid]:
                right = mid
            else:
                left = mid
        else:
            if nums[mid] <= target and target <= nums[right]:
                left = mid
            else:
                right = mid
    if nums[left] == target:                           # handling corner case if mid is the target
        return left                                    # like [5,1,3],5 expect output is 0(index)
    if nums[right] == target:
        return right
    return -1

# nums = [4,5,6,7,8,1,2,3]
# target = 8
# # expected outcome should be 4
# search(nums, target)

#-------------------------- another approach -------------------------

def search_1(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l + r)//2
        if target == nums[mid]:
            return mid

        if nums[l] <= nums[mid]:                                # the most important part in BS is to define mid
            if target > nums[mid] or target < nums[l]:          # in sorted array, if target>mid, left = mid 
                l = mid + 1                                     # in this particular case, two sorted parportions left and right
            else:                                               # we are compairing the upper bond of left sorted portion with target  
                r = mid - 1                                     # if greater than that,left pointer should move to mid
        
        else:
            if target < nums[mid] or target > nums[r]:          # right part is the same
                r = mid - 1
            else:
                l = mid + 1
    return -1