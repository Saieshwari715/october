class Solution:
    def sumOfUnique(self, num: List[int]) -> int:
        fre={}
        for i in num:
            if i in fre:
                fre[i]+=1
            else:
                fre[i]=1
        sum=0
        for key,value in fre.items():
            if(value==1):
                sum+=key
        return sum
            
        