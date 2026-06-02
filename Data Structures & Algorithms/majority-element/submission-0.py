class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicto={}
        for i in range(len(nums)):
            if nums[i] not in dicto:
                dicto[nums[i]]=1
            else:
                dicto[nums[i]]+=1
        for i in dicto:
            return max(dicto, key=dicto.get)
            