class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        kf = dict()
        for i in nums:
            if i not in kf:
                kf[i] = 1
            kf[i] += 1
        sorted_nums = sorted(kf, key=kf.get, reverse=True)
        return sorted_nums[:k]
# Time Complexity = O(nlogn)

# --- TRACE WALKTHROUGH EXAMPLE 2 ---
# Input: strs = ["a"]

# Step 1: Initialize empty dictionary
#   - new_strs = {}

# Step 2: Iterate through each word in strs
#   - word = "a": sorted_word = "a"
#       - "a" not in new_strs -> new_strs = {"a": []}
#       - append "a" -> new_strs = {"a": ["a"]}

# Step 3: Loop finishes, return dictionary values as a list
#   - list(new_strs.values()) 
#   - Returns [["a"]]