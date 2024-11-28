class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        max_dist = 0
        
        for idx, n in enumerate(nums):
            
            if max_dist < idx:
                return False
            
            max_dist = max(max_dist, idx + n)
      
            if max_dist >= goal:
                return True
                 
        return False