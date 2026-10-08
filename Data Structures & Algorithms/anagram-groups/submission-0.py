class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)


        return list(groups.values())


# first sort each string
# iterate through strings ahead of current index, seeing if it meets an anagram ahead
#   if an anagram is found, remove paired string from array and save it to sublist, and continue iterating
#   Once finished iterating, add original index to sublist and remove from array
#   add sublist to output array
# return output array
        