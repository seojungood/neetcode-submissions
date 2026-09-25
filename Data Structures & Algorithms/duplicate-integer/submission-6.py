class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. inefficient
        # for num in nums:
        #     if nums.count(num) > 1:
        #         return True
        # return False
        # 2. Also inefficient
        # for num in nums:
        #     if nums.count(num) != 1:
        #         return True
        # return False
        return len(nums) != len(set(nums))


            