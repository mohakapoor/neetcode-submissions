class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def drop_dots(arr: List[str]) -> List[str]:
            return [x for x in arr if x != "."]
        def check_array(arr: List[str]) -> List[str]:
            print(f"normal array: {drop_dots(arr)} unique array : {set(drop_dots(arr))}")
            return len(set(drop_dots(arr))) == len(drop_dots(arr))
        for i in range(0,9):
            arr = board[i]
            if check_array(arr) == False:
                return False
            arr = [row[i] for row in board]
            if check_array(arr) == False:
                return False
        for r in range(0,9,3):
            for c in range(0,9,3):
                arr = [i for row in board[r:r+3] for i in row[c:c+3]]
                if check_array(arr) == False:
                    return False
        return True