class Solution:
    #Only lowercase letters
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if lengths match
        if len(s)!=len(t): return False

        #Create Hashmaps
        counts, countt = {}, {}

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            countt[t[i]] = 1 + countt.get(t[i], 0)
        return counts ==  countt

        