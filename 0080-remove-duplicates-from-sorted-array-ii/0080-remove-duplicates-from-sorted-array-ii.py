class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        is_dup = False
        for j in range(1,len(nums)):
            if nums[i] == nums[j]:
                if not is_dup:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                    
                is_dup = True
                    
            else:
                i += 1
                is_dup = False
                nums[i], nums[j] = nums[j], nums[i]
          
        return i + 1
                