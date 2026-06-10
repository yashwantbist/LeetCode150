#Valid /sudoku
'''

You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true
Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

Optimal approach:
We can find the index of each square by the equation (row / 3) * 3 + (col / 3). Then we use hash set for O(1) lookups
 while inserting the number into its row, column and square it belongs to. We use separate hash maps for rows, columns, and squares.

'''
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # defaultdict(set) auto-creates an empty set for any new key
        # so we don't need to manually initialise rows[0], rows[1], etc.
        rows    = defaultdict(set)  # rows[r]    = digits seen in row r
        cols    = defaultdict(set)  # cols[c]    = digits seen in col c
        squares = defaultdict(set)  # squares[b] = digits seen in box b (0–8)

        for r in range(9):           # iterate over every row 0..8
            for c in range(9):       # iterate over every col 0..8

                val = board[r][c]    # current cell value, e.g. "5" or "."

                if val == ".":       # empty cell — skip it, nothing to validate
                    continue

                # ── compute which of the 9 boxes this cell belongs to ──────
                # integer division groups rows 0-2→0, 3-5→1, 6-8→2 (same for cols)
                # multiply row-group by 3 and add col-group → unique box id 0..8
                b = (r // 3) * 3 + (c // 3)

                # ── check for duplicates in all three containers at once ───
                if (val in rows[r] or      # already seen this digit in this row?
                    val in cols[c] or      # already seen this digit in this col?
                    val in squares[b]):    # already seen this digit in this box?
                    return False           # duplicate found → board is invalid

                # ── no duplicate yet → record this digit in all three sets ─
                rows[r].add(val)
                cols[c].add(val)
                squares[b].add(val)

        return True   # completed all 81 cells with no duplicates → valid


# ── Driver code ──────────────────────────────────────────────────────────────
solution = Solution()

board = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]

print(solution.isValidSudoku(board))   # True