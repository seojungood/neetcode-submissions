class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        # j = 1
        nums_map = dict()
        for num in nums:
            diff = target - nums[i]
            diff_index = nums_map.get(diff)
            if diff_index != None:
                return [diff_index,i]
            else:
                nums_map.update({num: i})
                i+=1
        return [i,i+1]
