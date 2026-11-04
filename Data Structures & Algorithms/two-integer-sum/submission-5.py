class Solution:
    #Every input has exactly one pair of indices that satisfy the condition
    #Return smaller index first
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Create hashmap
        seen = {}

        #Iterate through nums
        for i in range(len(nums)):
            #Calculate the needed number by subtracting current number in nums from target
            need = target - nums[i]
            #If the needed number is in seen, return need and current number
            if need in seen:
                return [seen[need], i]
            #Else add current number to seen
            seen[nums[i]] = i