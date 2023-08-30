from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = defaultdict(list)
        
        for i,j in enumerate(nums):
            dict[j].append(i)
                   
        nums.sort()
        
        l , r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] == target:
                if nums[l] == nums[r]:
                    return [dict[nums[l]][0],dict[nums[r]][1]]
                else:
                    return [dict[nums[l]][0],dict[nums[r]][0]]