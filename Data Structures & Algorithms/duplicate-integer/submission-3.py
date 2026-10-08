class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #    nums.sort()
    #    for i in range(1, len(nums)):
    #        if nums[i] == nums[i-1]:
    #            return True
    #    return False

        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

# create set seen
# for loop going through each value in array
    # if n in seen
        # return true
    # else add n to seen
# return false

