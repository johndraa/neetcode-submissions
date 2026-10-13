#contains only alphanumerics
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sorting strings
        sorteds = ''.join(sorted(s))
        sortedt = ''.join(sorted(t))

        #if the length of the two strings don't equal, answer is automatically false
        if len(sorteds) != len(sortedt): return False
        
        #comparing each character
        for i in range(len(s)):
            if sorteds[i] != sortedt[i]: return False
        return True
        