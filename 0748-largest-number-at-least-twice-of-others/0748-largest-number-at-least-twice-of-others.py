class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi=max(nums)
        max_in=nums.index(maxi)
        for i in range(len(nums)):
            if(nums[i]!=maxi and maxi<2*nums[i]):
                return -1
                break
        else:
            return max_in

        