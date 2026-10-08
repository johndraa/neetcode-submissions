# array has negative and positive integers
# array will have at least 3 integers
# no duplicate triplets
# return in any order
# return an empty output if no triplet equals 0
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, j in enumerate(nums):
            if j > 0: break #since nums is sorted, if j is positive all remaining nums are positive, so no triplet can = 0

            if i > 0 and j == nums[i-1]: continue #skip duplicates for first number

            l = i + 1  #left pointer
            r = len(nums) - 1 #right pointer
            while l < r:
                threeSum = j + nums[l] + nums[r]

                if threeSum > 0: r -= 1 #move r backward if sum is greater than zero
                elif threeSum < 0: l += 1 #move l forward if sum is less than zero
                else:
                    res.append([j, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: #skip duplicates on left side
                        l += 1
        return res