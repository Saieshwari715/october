class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0
        for i in sentences:
            a=i.split()
            c=len(a)
            maxi=max(maxi,c)
        return maxi



        