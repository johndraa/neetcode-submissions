class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(nums, target, 0, len(nums)-1)

    def binary(self, nums: List[int], target: int, start: int, end: int):
        
        if start > end: return -1
        
        middle = (start + end) // 2

        if nums[middle] == target: return middle

        if nums[middle] > target: return self.binary(nums, target, start, middle-1)

        if nums[middle] < target: return self.binary(nums, target, middle+1, end)