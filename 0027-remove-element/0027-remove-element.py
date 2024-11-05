class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        for i in range(len(nums)):
            if nums[0] == val:
                nums.remove(nums[0])
            else:
                nums.append(nums[0])
                nums.remove(nums[0])
                               
        return len(nums)