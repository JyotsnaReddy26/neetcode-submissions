class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        for value in freq.values():
            if value>1:
                return True
        
        return False

        

