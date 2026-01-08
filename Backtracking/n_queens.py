class NQueens:
    def __init__(self,n):
        self.n = n
        self.chess_table = [[0 for i in range(n) for j in range(n)]]
        