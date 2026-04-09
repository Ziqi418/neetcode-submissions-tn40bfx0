class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # what should I remember when I see "act" so that I can group it with "cat"
        # { tuple: [anagram1, anagram2] }
        map_strs = {}
        for str in strs:
            hash_str = tuple(sorted(str))
            if map_strs.get(hash_str):
                map_strs[hash_str].append(str)
            else:
                map_strs[hash_str] = [str]
        
        return list(map_strs.values())