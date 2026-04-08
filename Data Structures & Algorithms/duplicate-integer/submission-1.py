class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set
        set1 = set()
        for num in nums:
            if num in set1:
                return True
            set1.add(num)
        return False