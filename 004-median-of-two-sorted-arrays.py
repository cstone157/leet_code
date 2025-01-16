class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        count, prevN, currN, m, n = 0, -10**6, -10**6, len(nums1), len(nums2)
        maxN = m + n
        even = maxN % 2
        if even == 0:
            maxN = maxN / 2 + 1
        else:
            maxN = maxN / 2 + .5

        i, j = 0, 0
        if m > 0 and n > 0:
            while i + j < maxN:
                if i < m and nums1[i] >= currN and nums1[i] <= nums2[j]:
                    prevN = currN
                    currN = nums1[i]
                    i += 1
                    continue

                if nums2[j] >= currN:
                    prevN = currN
                    currN = nums2[j]
                    j += 1

                if i >= m or j >= n:
                    break

        if i + j < maxN:
            if i < m:
                while i + j < maxN:
                    prevN = currN
                    currN = nums1[i]
                    i += 1
            else:
                while i + j < maxN:
                    prevN = currN
                    currN = nums2[j]
                    j += 1

        if even == 1:
            return currN
        else:
            return (currN + prevN) / 2
