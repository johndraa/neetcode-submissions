class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(nums, target, 0, len(nums)-1)

    def binary(self, nums: List[int], target: int, start: int, end: int):

        #target not found
        if start > end:
            return -1
        
        #set middle to floor of section length/2
        middle = (start+end) // 2

        #if middle is bigger than target, set new section to be first half
        if nums[middle] > target: return self.binary(nums, target, 0, middle-1)

        #if middle is smaller than target, set new section to be second half
        elif nums[middle] < target: return self.binary(nums, target, middle+1, end)

        #target found
        else: return middle


        


        