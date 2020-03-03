class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Empty dict to hold differences between target and cur num
        diffs = {}

        for i, num in enumerate(nums):
            # num + diff = target 
            diff = target - num
            
            if diff in diffs: return [diffs[diff], i] # diff is found within dict

            # Note: add cur num to the dict after checking diff
            # Case: twoSum(self, [1, 1, 2], 2)
            diffs[num] = i
