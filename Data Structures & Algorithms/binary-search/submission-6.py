class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(nums, target, 0, len(nums)-1)

    def binary(self, nums: List[int], target: int, start: int, end: int):
        
        #target not found
        if start > end: return -1 
        
        #set middle to be the floor of section length/2
        middle = (start + end) // 2

        #if the middle is greater than target, create new section to be first half and search again
        if nums[middle] > target: return self.binary(nums, target, start, middle-1)

        #if the middle is less than target, create new section to be second half and search again
        elif nums[middle] < target: return self.binary(nums, target, middle+1, end)

        #target found
        else: return middle