class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window, with a dict to track duplicate chars
        char_count_map = {}
        max_substring_length = 0
        i, j = 0, 0
        while j < len(s):
            # if we can still extend the sequence:
            if not char_count_map.get(s[j]):
                char_count_map[s[j]] = 1
                j += 1
                max_substring_length = max(max_substring_length, j - i)
            else:
                char_count_map[s[i]] -= 1
                i += 1
            
        return max_substring_length
