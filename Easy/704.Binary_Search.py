# Definition for Binary Search implementation.

"""
===============================================================================
VISUALIZATION OF BINARY SEARCH EXECUTION & POINTER MOVEMENT
===============================================================================

Example 1: Target Exists (Success Case)
-------------------------------------------------------------------------------
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
Indices:        0   1  2  3  4   5

INITIAL STATE:
  left = 0, right = 5

-------------------------------------------------------------------------------
ITERATION 1:
  Pointers:   left = 0, right = 5
  Mid index:  mid = (0 + 5) // 2 = 2
  Value check: nums[2] is 3

  Visualization:
     0    1    2    3    4    5    (Indices)
   [-1,   0,   3,   5,   9,  12]
    ^          ^              ^
   left       mid           right

  Comparison:  nums[mid] (3) < target (9)
  Decision:    Target must be to the right of index 2.
               Update left = mid + 1  -->  left = 3

-------------------------------------------------------------------------------
ITERATION 2:
  Pointers:   left = 3, right = 5
  Mid index:  mid = (3 + 5) // 2 = 4
  Value check: nums[4] is 9

  Visualization:
     0    1    2    3    4    5    (Indices)
   [-1,   0,   3,   5,   9,  12]
                    ^    ^    ^
                  left  mid  right

  Comparison:  nums[mid] (9) == target (9)  --> MATCH FOUND!
  Output:      Return mid (4)

===============================================================================
Example 2: Target Does Not Exist (Failure Case)
-------------------------------------------------------------------------------
Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
Indices:        0   1  2  3  4   5

Iter 1: left = 0, right = 5 | mid = 2 (val = 3) | 3 > 2  --> right = mid - 1 = 1
Iter 2: left = 0, right = 1 | mid = 0 (val = -1)| -1 < 2 --> left = mid + 1 = 1
Iter 3: left = 1, right = 1 | mid = 1 (val = 0) | 0 < 2  --> left = mid + 1 = 2

Loop Condition Check: left (2) <= right (1) is FALSE. Loop ends.
Output: Return -1
===============================================================================
"""


class Solution:

    def search(self, nums: list[int], target: int) -> int:
        # Initialize search range to encompass the entire array
        left = 0
        right = len(nums) - 1

        # Continue search as long as the search window is valid (pointers haven't crossed)
        while left <= right:
            # Find the midpoint of the current search window
            mid = (left + right) // 2

            # 1. Target found: return its array index directly
            if nums[mid] == target:
                return mid

            # 2. Mid value is smaller than target: target must lie in the right half
            if nums[mid] < target:
                left = mid + 1

            # 3. Mid value is larger than target: target must lie in the left half
            if nums[mid] > target:
                right = mid - 1

        # Search window closed without finding target
        return -1