class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # need to return the position, no sorting
        # use a pointer i, we have nums[i], the goal is to find (target - nums[i]) in the rest
        nums_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            num_goal = target - num
            if nums_dict.get(num_goal) is not None:
                return [nums_dict[num_goal], i]

            nums_dict.setdefault(num, i)
        return [-1, -1]