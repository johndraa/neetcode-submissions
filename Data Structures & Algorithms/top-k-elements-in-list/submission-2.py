class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for num in nums:
            occ[num] = occ.get(num, 0) + 1
        top = sorted(occ.items(), key=lambda kv: kv[1], reverse=True)[:k]
        return [key for key, val in top]
        
        

#iterate through nums
# take first integer encountered, count the number of occurences, save it
# move on to next integer encountered, count the number of occurences save it
# keep going until all unique integers are found
# return the top k appearances in an array