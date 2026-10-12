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


# --- TRACE WALKTHROUGH EXAMPLE ---
# Input: s = "cat", t = "tac"

# 1. Sorting:
#    - sorted("cat") -> ['a', 'c', 't']
#    - sorted("tac") -> ['a', 'c', 't']

# 2. Comparison:
#    - ['a', 'c', 't'] == ['a', 'c', 't'] -> TRUE!
#    - Returns True

# --- TRACE WALKTHROUGH EXAMPLE ---
# Input: s = "cat", t = "tac"

# Step 1: len("cat") == len("tac") (3 == 3) -> Continue

# Step 2: Count characters in s = "cat"
#   - char = 'c' -> char_counts = {'c': 1}
#   - char = 'a' -> char_counts = {'c': 1, 'a': 1}
#   - char = 't' -> char_counts = {'c': 1, 'a': 1, 't': 1}

# Step 3: Decrement counts using t = "tac"
#   - char = 't': 't' in char_counts (count: 1) -> valid -> char_counts['t'] becomes 0
#   - char = 'a': 'a' in char_counts (count: 1) -> valid -> char_counts['a'] becomes 0
#   - char = 'c': 'c' in char_counts (count: 1) -> valid -> char_counts['c'] becomes 0

# Step 4: Loop finishes without returning False -> Returns True