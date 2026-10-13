class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        new_strs = dict()

        for word in strs:
            
            sorted_word = ''.join(sorted(word))

            if sorted_word not in new_strs:
                new_strs[sorted_word] = []
                
            new_strs[sorted_word].append(word)
        
        return list(new_strs.values())
# Time Complexity: O(N*K)

# --- TRACE WALKTHROUGH EXAMPLE 1 ---
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Step 1: Initialize empty dictionary
#   - new_strs = {}

# Step 2: Iterate through each word in strs
#   - word = "eat": sorted_word = "aet"
#       - "aet" not in new_strs -> new_strs = {"aet": []}
#       - append "eat" -> new_strs = {"aet": ["eat"]}
#
#   - word = "tea": sorted_word = "aet"
#       - "aet" in new_strs (valid)
#       - append "tea" -> new_strs = {"aet": ["eat", "tea"]}
#
#   - word = "tan": sorted_word = "ant"
#       - "ant" not in new_strs -> new_strs = {"aet": ["eat", "tea"], "ant": []}
#       - append "tan" -> new_strs = {"aet": ["eat", "tea"], "ant": ["tan"]}
#
#   - word = "ate": sorted_word = "aet"
#       - "aet" in new_strs (valid)
#       - append "ate" -> new_strs = {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}
#
#   - word = "nat": sorted_word = "ant"
#       - "ant" in new_strs (valid)
#       - append "nat" -> new_strs = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}
#
#   - word = "bat": sorted_word = "abt"
#       - "abt" not in new_strs -> new_strs = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"], "abt": []}
#       - append "bat" -> new_strs = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"], "abt": ["bat"]}

# Step 3: Loop finishes, return dictionary values as a list
#   - list(new_strs.values()) 
#   - Returns [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]