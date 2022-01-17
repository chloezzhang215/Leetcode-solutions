class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s or len(s) == 0 or k > len(s):
            return 0
        hset = set(['a','e','i','o','u'])
        res,count = 0,0

        for i in range(k):
            if s[i] in hset:
                count += 1
        res = max(res,count)

        for i in range(k, len(s)):
            out = s[i-k]
            inc = s[i]
            if out in hset:
                count -= 1
            if inc in hset:
                count += 1
            res = max(res,count)

        return res
