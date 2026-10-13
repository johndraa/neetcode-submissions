#contains only alphanumerics
#contains only lowercase
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the length of the two strings don't equal, answer is automatically false
        if len(s) != len(t): return False
        
        #sorting strings
        sorteds = ''.join(sorted(s))
        sortedt = ''.join(sorted(t))
        
        #comparing each character
        for i in range(len(s)):
            if sorteds[i] != sortedt[i]: return False
        return True
        