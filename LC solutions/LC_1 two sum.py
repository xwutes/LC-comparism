#LC_1 two sum
def twoSum(nums,target):
    ht = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in ht:
            return ht[diff],i
        ht[n] = i

nums = [2,7,11,15]
target = 26
twoSum(nums,target)