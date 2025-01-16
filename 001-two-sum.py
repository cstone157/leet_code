class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for j in range(len(nums)):
        #    n = nums[j]
        #    for k in range(j+1, len(nums)):
        #        if (n + nums[k]) == target:
        #            return [j, k]
        
        #return None
        seen = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [i, seen[complement]]
            seen[n] = i
        return None
