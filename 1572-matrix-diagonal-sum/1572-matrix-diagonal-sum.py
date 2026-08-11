class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        '''
        for interview rounds prefer this code 
        n=len(mat)
        total=0
        for i in range(n):
            total+=mat[i][i]
            total+=mat[i][n-1-i]
        if n%2==1:
            total-=mat[n//2][n//2]
        return total 
        '''
        n = len(mat)

        total = sum(mat[i][i] + mat[i][n - 1 - i] for i in range(n))

        if n % 2:
            total -= mat[n // 2][n // 2]

        return total