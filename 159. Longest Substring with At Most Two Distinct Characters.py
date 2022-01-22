class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0

        max_len = 0 
        hmap = {}

        start = 0
        for end in range(len(s)):
            hmap[s[end]] = hmap.get(s[end], 0)+1
            if len(hmap) <= 2:
                max_len = max(max_len,end - start + 1)
            
            while len(hmap) > 2:
                hmap[s[start]] -= 1
                if hmap[s[start]] == 0:
                    del(hmap[s[start]])
                start += 1
            
        return max_len

