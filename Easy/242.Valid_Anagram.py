# s = cat t = tac -- TRUE
# s = sam t = sat -- FALSE
# Every single piece of character in this 2 variable
# is the same then false if not
# 0(n^)

# FIRST SOLUTION O(nlogn)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True
        else:
            return False

# SECOND SOLUTION

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counts = {}

        for char in s:
            char_counts[char] = char_counts.get(char,0) + 1

        for char in t:
            if char not in char_counts or char_counts[char] == 0:
                return False
            char_counts[char] -= 1

        return True

