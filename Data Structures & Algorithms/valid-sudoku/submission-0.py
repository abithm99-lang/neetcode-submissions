class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #go to all the rows put it in a hashset check if any occur if yes return false
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) 
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
                
        return True
        
        