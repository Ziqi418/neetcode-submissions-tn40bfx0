class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # need to find all possible sequences before return

        # brutal force
        # take each num, find if it has 'next element' in the array, extend the sequence if yes
        # 
        # to achieve O(n), we need to remember what we have seen as we go through the array
        # using a DS faster to read than O(n)

        # what's interesting about O(n) is that I don't have to do everything in a loop.
        # It can be multiple O(n)

        nums_set = set(nums) # O(n)
        max_sequence_count = 0
        for num in nums:
            if (num - 1) not in nums_set:
                # check if num + 1, num + 2, ... is in the set
                sequence_count = 1
                while (num + sequence_count) in nums_set:
                    sequence_count += 1
                max_sequence_count = max(max_sequence_count, sequence_count)

        return max_sequence_count

