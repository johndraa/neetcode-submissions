class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if lengths match
        if len(s)!=len(t): return False

        #Sort and return true if they match, false if not
        return sorted(s) == sorted(t)
        