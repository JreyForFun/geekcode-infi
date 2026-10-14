class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        left = [1] * n
        right = [1] * n
        res = [1] * n

        for i in range(1,n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        for i in range(n):
            res[i] = left[i] * right[i]

        return res 

# Time Complexity: O(N)
# Space Complexity: O(N)

# --- TRACE WALKTHROUGH EXAMPLE 1 ---
# Input: nums = [1, 2, 3, 4]

# Step 1: Initialize length and pre-fill arrays with 1s
#   - n = 4
#   - left =  [1, 1, 1, 1]
#   - right = [1, 1, 1, 1]
#   - res =   [1, 1, 1, 1]

# Step 2: Iterate forward to build the `left` array (products to the left of i)
#   - Loop i in range(1, 4):
#
#   - i = 1: 
#       - left[1] = left[0] * nums[0] -> 1 * 1 = 1
#       - left array updates -> [1, 1, 1, 1]
#
#   - i = 2: 
#       - left[2] = left[1] * nums[1] -> 1 * 2 = 2
#       - left array updates -> [1, 1, 2, 1]
#
#   - i = 3: 
#       - left[3] = left[2] * nums[2] -> 2 * 3 = 6
#       - left array updates -> [1, 1, 2, 6]

# Step 3: Iterate backward to build the `right` array (products to the right of i)
#   - Loop i in range(2, -1, -1):
#
#   - i = 2: 
#       - right[2] = right[3] * nums[3] -> 1 * 4 = 4
#       - right array updates -> [1, 1, 4, 1]
#
#   - i = 1: 
#       - right[1] = right[2] * nums[2] -> 4 * 3 = 12
#       - right array updates -> [1, 12, 4, 1]
#
#   - i = 0: 
#       - right[0] = right[1] * nums[1] -> 12 * 2 = 24
#       - right array updates -> [24, 12, 4, 1]

# Step 4: Iterate to multiply left and right products into `res`
#   - Loop i in range(4):
#
#   - i = 0: 
#       - res[0] = left[0] * right[0] -> 1 * 24 = 24
#       - res array updates -> [24, 1, 1, 1]
#
#   - i = 1: 
#       - res[1] = left[1] * right[1] -> 1 * 12 = 12
#       - res array updates -> [24, 12, 1, 1]
#
#   - i = 2: 
#       - res[2] = left[2] * right[2] -> 2 * 4 = 8
#       - res array updates -> [24, 12, 8, 1]
#
#   - i = 3: 
#       - res[3] = left[3] * right[3] -> 6 * 1 = 6
#       - res array updates -> [24, 12, 8, 6]

# Step 5: Loop finishes, return the res array
#   - return res
#   - Returns [24, 12, 8, 6]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        # 1. Build the left products directly inside `res`
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # 2. Multiply the right products on the fly using a single variable
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res

# Time Complexity: O(N)
# Space Complexity: O(1) Extra Space (Excluding the output array `res`)

# --- TRACE WALKTHROUGH EXAMPLE 1 ---
# Input: nums = [1, 2, 3, 4]

# Step 1: Initialize the output array and length
#   - n = 4
#   - res = [1, 1, 1, 1]

# Step 2: Forward Pass - Build `prefix` products directly inside `res`
#   - prefix = 1
#   - Loop i in range(4):
#
#   - i = 0 (nums[0] = 1): 
#       - res[0] = prefix -> 1
#       - prefix = prefix * nums[0] -> 1 * 1 = 1
#       - res array updates -> [1, 1, 1, 1]
#
#   - i = 1 (nums[1] = 2): 
#       - res[1] = prefix -> 1
#       - prefix = prefix * nums[1] -> 1 * 2 = 2
#       - res array updates -> [1, 1, 1, 1]
#
#   - i = 2 (nums[2] = 3): 
#       - res[2] = prefix -> 2
#       - prefix = prefix * nums[2] -> 2 * 3 = 6
#       - res array updates -> [1, 1, 2, 1]
#
#   - i = 3 (nums[3] = 4): 
#       - res[3] = prefix -> 6
#       - prefix = prefix * nums[3] -> 6 * 4 = 24
#       - res array updates -> [1, 1, 2, 6]
#
#   (Notice how `res` now holds the exact same values as your old `left` array)

# Step 3: Backward Pass - Multiply `suffix` products on the fly
#   - suffix = 1
#   - Loop i in range(3, -1, -1):
#
#   - i = 3 (nums[3] = 4): 
#       - res[3] = res[3] * suffix -> 6 * 1 = 6
#       - suffix = suffix * nums[3] -> 1 * 4 = 4
#       - res array updates -> [1, 1, 2, 6]
#
#   - i = 2 (nums[2] = 3): 
#       - res[2] = res[2] * suffix -> 2 * 4 = 8
#       - suffix = suffix * nums[2] -> 4 * 3 = 12
#       - res array updates -> [1, 1, 8, 6]
#
#   - i = 1 (nums[1] = 2): 
#       - res[1] = res[1] * suffix -> 1 * 12 = 12
#       - suffix = suffix * nums[1] -> 12 * 2 = 24
#       - res array updates -> [1, 12, 8, 6]
#
#   - i = 0 (nums[0] = 1): 
#       - res[0] = res[0] * suffix -> 1 * 24 = 24
#       - suffix = suffix * nums[0] -> 24 * 1 = 24
#       - res array updates -> [24, 12, 8, 6]

# Step 4: Loop finishes, return the res array
#   - return res
#   - Returns [24, 12, 8, 6]