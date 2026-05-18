class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_array(arr: List[str]) -> List[str]:
            arr = [x for x in arr if x != "."]
            return len(set(arr)) == len(arr)
        for i in range(0,9):
            arr = board[i]
            if not check_array(arr) : return False
            arr = [row[i] for row in board]
            if not check_array(arr) : return False
        for r in range(0,9,3):
            for c in range(0,9,3):
                arr = [i for row in board[r:r+3] for i in row[c:c+3]]
                if not check_array(arr) : return False
        return True