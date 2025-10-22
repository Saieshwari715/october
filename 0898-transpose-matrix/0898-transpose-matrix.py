class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l=[]
        m,n=len(matrix),len(matrix[0])
        for j in range(n):
            r=[]
            for i in range(m):
                r.append(matrix[i][j])
            l.append(r)
        return l


        