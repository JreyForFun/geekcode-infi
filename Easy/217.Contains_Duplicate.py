class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

# time: 0(n log n)

# --- TRACE WALKTHROUGH EXAMPLE ---
# Input: nums = [1, 2, 3, 1]

# 1. nums.sort()
#    - Array becomes: [1, 1, 2, 3]

# 2. Loop Execution:
#    - i = 1 | nums[1] = 1, nums[0] = 1
#      -> Check: nums[1] == nums[0] (1 == 1) -> TRUE!
#      -> Immediately return True (Duplicate found)