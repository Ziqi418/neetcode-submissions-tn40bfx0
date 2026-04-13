class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # how do I deal with this 'unlimited number of times'?
        # given 2, I'm looking for a 7
        nums = sorted(nums)
        res = []
        def solve(remaining_target: int, current_path: List, start_index: int) -> None:
            if start_index > len(nums) - 1:
                return
            for i in range(start_index, len(nums)):
                if nums[i] == remaining_target:
                    current_path.append(nums[i])
                    res.append(current_path[:])
                    current_path.pop()
                elif nums[i] < remaining_target:
                    current_path.append(nums[i])
                    solve(remaining_target - nums[i], current_path, i)
                    current_path.pop()
                else:
                    break
        solve(target, [], 0)
        return res