"""
===============================================================================
COMPREHENSIVE VISUALIZATION & IN-DEPTH WALKTHROUGH
===============================================================================

To truly understand how these algorithms behave, we need a larger array where 
the "lead" changes back and forth. 

Let's use the array: nums = [2, 2, 1, 1, 1, 2, 2]
Total elements (n) = 7
Required for majority (⌊n/2⌋) = >3 appearances.
The majority element is 2 (appears 4 times).

-------------------------------------------------------------------------------
APPROACH 1: Hash Map / Dictionary [ Time: O(n), Space: O(n) ]
-------------------------------------------------------------------------------
Explanation:
This approach relies on counting. We create a dictionary `d` where the "key" is 
the number from the array, and the "value" is how many times we've seen it.
- `d.get(num, 0)` checks the dictionary for `num`. If it exists, it returns its 
  current count. If it doesn't exist yet, it returns 0.
- We add 1 to that count and save it.
- Finally, `max(d, key=d.get)` iterates through all the keys in the dictionary 
  and returns the one that maps to the largest value.

Full Iteration Visualization for nums = [2, 2, 1, 1, 1, 2, 2]:

Index | Current 'num' | Dictionary Update Calculation   | Dictionary State 'd' After
--------------------------------------------------------------------------------------
  0   |      2        | d[2] = d.get(2, 0) + 1  -> 1    | {2: 1}
  1   |      2        | d[2] = d.get(2, 1) + 1  -> 2    | {2: 2}
  2   |      1        | d[1] = d.get(1, 0) + 1  -> 1    | {2: 2, 1: 1}
  3   |      1        | d[1] = d.get(1, 1) + 1  -> 2    | {2: 2, 1: 2}
  4   |      1        | d[1] = d.get(1, 2) + 1  -> 3    | {2: 2, 1: 3}
  5   |      2        | d[2] = d.get(2, 2) + 1  -> 3    | {2: 3, 1: 3}
  6   |      2        | d[2] = d.get(2, 3) + 1  -> 4    | {2: 4, 1: 3}

Final Evaluation: 
max({2: 4, 1: 3}, key=d.get) 
- 2 has a count of 4.
- 1 has a count of 3.
Output -> 2.


-------------------------------------------------------------------------------
APPROACH 2: Boyer-Moore Voting Algorithm [ Time: O(n), Space: O(1) ]
(Using `res` and `majority` variables)
-------------------------------------------------------------------------------
Explanation:
Because the majority element is mathematically guaranteed to appear MORE than 
half the time, if every majority element paired up and "destroyed" a non-majority 
element, the majority element would still have survivors left over.

- `res` holds our current presumed majority element.
- `majority` is our "confidence score" or the number of "lives" the candidate has.
- If `majority == 0`, we have no confidence in our current `res`, so we adopt the 
  current `num` as our new `res`.
- If the current `num` is the same as `res`, our confidence grows (+1).
- If the current `num` is different from `res`, they fight, and confidence drops (-1).

Full Iteration Visualization for nums = [2, 2, 1, 1, 1, 2, 2]:

Idx | num | majority | Is majority == 0? | res | Is num == res? | majority
    |     | (Start)  |                   |     |                | (End)
-------------------------------------------------------------------------------
 0  |  2  |    0     | YES -> res = 2    |  2  | 2==2 (YES) +1  |    1
 1  |  2  |    1     | NO                |  2  | 2==2 (YES) +1  |    2
 2  |  1  |    2     | NO                |  2  | 1==2 (NO)  -1  |    1
 3  |  1  |    1     | NO                |  2  | 1==2 (NO)  -1  |    0   <-- Lost all confidence
 4  |  1  |    0     | YES -> res = 1    |  1  | 1==1 (YES) +1  |    1   <-- 1 takes over!
 5  |  2  |    1     | NO                |  1  | 2==1 (NO)  -1  |    0   <-- Lost all confidence
 6  |  2  |    0     | YES -> res = 2    |  2  | 2==2 (YES) +1  |    1   <-- 2 takes back over!

Loop ends. The final value held in `res` is 2.
Output -> 2.


-------------------------------------------------------------------------------
APPROACH 3: Boyer-Moore Voting Algorithm [ Time: O(n), Space: O(1) ]
(Using `candidate` and `count` variables)
-------------------------------------------------------------------------------
Explanation:
This is the exact same mathematical logic as Approach 2, but it is written with 
cleaner, industry-standard variable names. 

Additionally, it initializes `candidate = None`. 
Why? Because in Python, `res = majority = 0` initializes `res` to the integer 0. 
If the array contains the number 0 (e.g., nums = [0, 0, 1]), initializing `res` 
to 0 can technically cause slight confusion during debugging since 0 is both the 
default state AND a valid array value. Starting with `None` explicitly indicates 
that the candidate hasn't been chosen yet.

Full Iteration Visualization for nums = [2, 2, 1, 1, 1, 2, 2]:

Idx | num | count   | Is count == 0?       | candidate | Is num == candidate? | count
    |     | (Start) |                      |           |                      | (End)
-------------------------------------------------------------------------------------
 0  |  2  |   0     | YES -> cand = 2      |     2     | 2==2 (YES) -> +1     |   1
 1  |  2  |   1     | NO                   |     2     | 2==2 (YES) -> +1     |   2
 2  |  1  |   2     | NO                   |     2     | 1==2 (NO)  -> -1     |   1
 3  |  1  |   1     | NO                   |     2     | 1==2 (NO)  -> -1     |   0
 4  |  1  |   0     | YES -> cand = 1      |     1     | 1==1 (YES) -> +1     |   1
 5  |  2  |   1     | NO                   |     1     | 2==1 (NO)  -> -1     |   0
 6  |  2  |   0     | YES -> cand = 2      |     2     | 2==2 (YES) -> +1     |   1

Loop ends. The final value held in `candidate` is 2.
Output -> 2.
===============================================================================
"""

# -----------------
# CODE DEFINITIONS
# -----------------

# APPROACH 1
class Solution1:
    def majorityElement(self, nums: list[int]) -> int:
        d = dict()
        for num in nums:
            d[num] = d.get(num, 0) + 1
        return max(d, key=d.get)

# APPROACH 2
class Solution2:
    def majorityElement(self, nums: list[int]) -> int:
        res = majority = 0
        for num in nums:
            if majority == 0:
                res = num
            majority += 1 if num == res else -1
        return res 

# APPROACH 3
class Solution3:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate