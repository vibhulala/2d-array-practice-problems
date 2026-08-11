class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        '''
        Toh brute force mein hum sorted property completely ignore kar rahe hain
        is liye ye brute force sirf normal understandind ke liy ehain 
        hence  hm question me used propety ki help leke apna code design karenge
        count=0
        for i in range(len(grid)):
            for  j in range(len(grid[0])):
                if grid[i][j]<0:
                    count+=1
        return count 
        '''
        m = len(grid)
        n = len(grid[0])

        row = m - 1
        col = 0
        count = 0

        while row >= 0 and col < n:

            if grid[row][col] < 0:
                count += n - col
                row -= 1

            else:
                col += 1

        return count