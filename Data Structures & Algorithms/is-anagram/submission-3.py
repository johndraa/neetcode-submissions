class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if lengths match
        if len(s)!=len(t): return False

        #Sort strings
        sorteds = ''.join(sorted(s))
        sortedt = ''.join(sorted(t))

        #Return true if they match, false if not
        return sorteds == sortedt
        