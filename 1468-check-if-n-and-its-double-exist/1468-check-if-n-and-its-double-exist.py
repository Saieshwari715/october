class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        f=False
        for i in range(len(arr)):
            s=arr[i]//2
            if s in arr and arr[i]%2==0 and i != arr.index(s):
                f=True
                break
        return f