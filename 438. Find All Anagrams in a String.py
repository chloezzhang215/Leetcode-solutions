class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        hmap = {}

        hmap_p = {}
        for char in p:
            hmap_p[char] = hmap_p.get(char,0) + 1
        
        start = 0
        for end in range(len(s)):
            hmap[s[end]] = hmap.get(s[end],0) + 1
            if hmap == hmap_p:
                res.append(start)

            if end >= len(p) - 1:
                hmap[s[start]] -= 1
                if hmap[s[start]] == 0:
                    del(hmap[s[start]])
                start += 1
        
        return res
