class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum1=sum(aliceSizes)
        sum2=sum(bobSizes)
        dif=(sum1-sum2)//2
        for i in aliceSizes:
            j=i-dif
            if j in bobSizes:
                return [i,j]