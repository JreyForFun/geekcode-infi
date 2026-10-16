class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        N = 9
        rows = [None] * N
        cols = [None] * N
        boxes = [None] * N

        for r in range(N):
            rows[r] = set()
            cols[r] = set()
            boxes[r] = set()

        for r in range(N):
            for c in range(N):
                val = board[r][c]

                if val == ".":
                    continue
                if val in rows[r]:
                    return False
                
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                idx = (r // 3) * 3 + (c // 3)
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
        return True

# Time Complexity = O(N^2) (Effectively O(1) since N is always 9)
# Space Complexity = O(N^2) (Effectively O(1) for the 27 hash sets)

# --- TRACE WALKTHROUGH EXAMPLE 2 ---
# Input: board where top-left 3x3 box contains:
# r=0: ["8", "3", ".", ...]
# r=1: ["6", ".", ".", ...]
# r=2: [".", "9", "8", ...] <-- Duplicate "8" at r=2, c=2

# Step 1: Initialize lists of 9 empty sets
#   - rows = [set(), set(), ..., set()]
#   - cols = [set(), set(), ..., set()]
#   - boxes = [set(), set(), ..., set()]

# Step 2: Iterate through each cell in the 9x9 board
#   - r = 0, c = 0: val = "8"
#       - Not "." -> proceed
#       - "8" not in rows[0] -> rows[0].add("8") -> rows[0] = {"8"}
#       - "8" not in cols[0] -> cols[0].add("8") -> cols[0] = {"8"}
#       - idx = (0 // 3) * 3 + (0 // 3) = 0
#       - "8" not in boxes[0] -> boxes[0].add("8") -> boxes[0] = {"8"}

#   - r = 0, c = 1: val = "3"
#       - Not "." -> proceed
#       - "3" not in rows[0] -> rows[0].add("3") -> rows[0] = {"8", "3"}
#       - "3" not in cols[1] -> cols[1].add("3") -> cols[1] = {"3"}
#       - idx = (0 // 3) * 3 + (1 // 3) = 0
#       - "3" not in boxes[0] -> boxes[0].add("3") -> boxes[0] = {"8", "3"}

#   - (Skipping empty "." cells) ...

#   - r = 1, c = 0: val = "6"
#       - Not "." -> proceed
#       - "6" not in rows[1] -> rows[1].add("6") -> rows[1] = {"6"}
#       - "6" not in cols[0] -> cols[0].add("6") -> cols[0] = {"8", "6"}
#       - idx = (1 // 3) * 3 + (0 // 3) = 0
#       - "6" not in boxes[0] -> boxes[0].add("6") -> boxes[0] = {"8", "3", "6"}

#   - r = 2, c = 1: val = "9"
#       - Not "." -> proceed
#       - "9" not in rows[2] -> rows[2].add("9") -> rows[2] = {"9"}
#       - "9" not in cols[1] -> cols[1].add("9") -> cols[1] = {"3", "9"}
#       - idx = (2 // 3) * 3 + (1 // 3) = 0
#       - "9" not in boxes[0] -> boxes[0].add("9") -> boxes[0] = {"8", "3", "6", "9"}

#   - r = 2, c = 2: val = "8"
#       - Not "." -> proceed
#       - "8" not in rows[2] -> rows[2].add("8") -> rows[2] = {"9", "8"}
#       - "8" not in cols[2] -> cols[2].add("8") -> cols[2] = {"8"}
#       - idx = (2 // 3) * 3 + (2 // 3) = 0
#       - Check: is "8" in boxes[0]? 
#           - YES! boxes[0] currently contains {"8", "3", "6", "9"}
#           - Rule broken: Sub-box contains duplicate!

# Step 3: Function terminates early
#   - Returns False