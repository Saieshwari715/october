class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        l=[[0 for _ in range(n)]for _ in range(m)]
        for r,c in indices:
            for j in range(n):
                l[r][j]+=1
            for i in range(m):
                l[i][c]+=1
        c=0
        for i in range(m):
            for j in range(n):
                if l[i][j]%2!=0:
                    c+=1
        return c

          