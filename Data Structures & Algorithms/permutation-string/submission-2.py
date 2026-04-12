class Solution:
    from collections import Counter

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we know: length of s1, so we should fix a window of len(s1), find if there's a permutation of s1
        # once we have the window, how do we compare s1 and this window?
        # "abc" "cab" -> convert to set and compare?
        if len(s1) > len(s2):
            return False

        m = len(s1)
        s1_count = Counter(s1)
        window = Counter(s2[:m])
        if s1_count == window:
            return True

        for i in range(m, len(s2)):
            window[s2[i]] += 1
            left_char = s2[i - m]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if s1_count == window:
                return True
        
        return False
