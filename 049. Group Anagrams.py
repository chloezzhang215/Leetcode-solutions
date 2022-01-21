class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)

        for char in strs:
            key = "".join(sorted(char))
            hmap[key].append(char)
        
        return list(hmap.values())
