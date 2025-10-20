class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        def firstocc(nums,target,n):
            low=0
            high=n-1
            first=-1
            while(low<=high):
                mid=(low+high)//2
                if(nums[mid]==target):
                    first=mid
                    high=mid-1
                elif(nums[mid]<target):
                    low=mid+1
                else:
                    high=mid-1
            return first
        def lastocc(nums,target,n):
            low=0
            high=n-1
            last=-1
            while(low<=high):
                mid=(low+high)//2
                if(nums[mid]==target):
                    last=mid
                    low=mid+1
                elif(nums[mid]<target):
                    low=mid+1
                else:
                    high=mid-1
            return last
        first=firstocc(nums,target,n)
        last=lastocc(nums,target,n)
        if(first==-1):
            return[-1,-1]
        return [first,last]

        