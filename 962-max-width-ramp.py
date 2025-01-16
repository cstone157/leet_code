class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        to_return = 0
        stack = []
        n = len(nums)

        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                to_return = max(to_return, j - i)

        return to_return
