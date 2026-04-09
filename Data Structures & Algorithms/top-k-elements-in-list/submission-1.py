class Solution:
    from collections import Counter
    import heapq

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # to use heap, we need the frequency first
        count = Counter(nums) # num: frequency

        heap = []

        for num in count:
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [h[1] for h in heap]
