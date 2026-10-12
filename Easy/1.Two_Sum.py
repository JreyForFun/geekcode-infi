class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        O(n) speed
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff = dict()
        
        for i in range(len(nums)):
            find = target - nums[i]
            if find in diff:
                return [diff[find], i]
            diff[nums[i]] = i

        return []

# --- TRACE WALKTHROUGH EXAMPLE ---
# Example: nums = [3, 2, 4], target = 6
#
# i = 0 | nums[0] = 3
#   - find = 6 - 3 = 3
#   - Is 3 in diff? No (diff is currently {})
#   - Store: diff[3] = 0 -> diff is now {3: 0}
#
# i = 1 | nums[1] = 2
#   - find = 6 - 2 = 4
#   - Is 4 in diff? No (diff is currently {3: 0})
#   - Store: diff[2] = 1 -> diff is now {3: 0, 2: 1}
#
# i = 2 | nums[2] = 4
#   - find = 6 - 4 = 2
#   - Is 2 in diff? YES! diff[2] gives index 1.
#   - Return [1, 2]