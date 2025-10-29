class Solution:
    def findLucky(self, num: List[int]) -> int:
        fre={}
        for i in num:
            if i in fre:
                fre[i]+=1
            else:
                fre[i]=1
        maxi=0
        for key,val in fre.items():
            if(key==val):
                maxi=max(key,maxi)
        if maxi==0:
            return -1
        return maxi
        