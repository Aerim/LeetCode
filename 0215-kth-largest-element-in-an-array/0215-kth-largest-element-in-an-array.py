class Solution(object):
    def findKthLargest(self, nums, k):

        counts = [0] * (20001)

        for num in nums:
            idx = num
            counts[idx + 10000] += 1

        for i in range(1, len(counts)):
            counts[i] = counts[i] + counts[i - 1]
            
        result = [0] * len(nums)

        for num in nums:
            idx = counts[num + 10000] 
            result[idx - 1] = num
            counts[num + 10000] -= 1

        return result[-k]

        