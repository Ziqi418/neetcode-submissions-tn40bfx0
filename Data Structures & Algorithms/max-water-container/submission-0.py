class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # amount of water = (j - i) * min(height[i], height[j])
        # start by i = 0, j = len(heights) - 1
        # decide when to move i or j, if height[i] < height[j], move i
        i, j = 0, len(heights) - 1
        max_volume_water = 0
        while i < j:
            volume_water = (j - i) * min(heights[i], heights[j])
            max_volume_water = max(max_volume_water, volume_water)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_volume_water