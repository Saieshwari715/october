class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in details:
            s=""
            for j in i[11:13]:
                s+=j
                if(int(s)>60):
                    c+=1
        return c
        