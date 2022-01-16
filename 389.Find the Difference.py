class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 利用字典
        # d = {}
        # for i in s:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        
        # for i in t:
        #     if i in d:
        #         if d[i] == 0:return i
        #         d[i] -= 1
        #    else:
        #         return i

        # 位运算
        ans = 0
        for i in s:
            ans ^= ord(i)

        for i in t:
             ans ^= ord(i)
        
        return chr(ans)
