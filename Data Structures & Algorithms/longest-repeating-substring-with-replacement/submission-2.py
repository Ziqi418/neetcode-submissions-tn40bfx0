class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # build a dict to track occurrence
        # {A: 4, B: 3, C: 2, D: 1}
        s_counter = {}
        max_occurrence = 0
        max_window_size = 0
        i = 0
        for j in range(len(s)):
            if not s_counter.get(s[j]):
                s_counter[s[j]] = 1
            else:
                s_counter[s[j]] += 1
            max_occurrence = max(max_occurrence, s_counter[s[j]])
            
            if (j - i + 1) - max_occurrence > k:
                s_counter[s[i]] -= 1
                i += 1
            max_window_size = max(max_window_size, j - i + 1)
                
        return max_window_size