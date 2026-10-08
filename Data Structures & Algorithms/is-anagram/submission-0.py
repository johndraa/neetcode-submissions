# not checking for capitalization, order doesnt matter, is string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sorts = "".join(sorted(s))
        sortt = "".join(sorted(t))
        return sorts == sortt
    # check if str lengths match, return false if they dont
    # sort the strings alphabetically
    # iterate through s string
    #   if character at i in s does not match character at i in t       #        return false
    #return true

    