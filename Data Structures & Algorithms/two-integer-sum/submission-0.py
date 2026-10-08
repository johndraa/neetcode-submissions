# assume each input has at least one pair of indices that satisfies condition
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    arr = []
                    arr.append(i)
                    arr.append(j)
                    return arr
    # iterate through nums
    #  iterate through nums+1
            # add i to j, if they equal the target number then add the      # indices to a new array and return