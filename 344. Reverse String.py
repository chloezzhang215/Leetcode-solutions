class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a = 0
        b = len(s) - 1
        while a < b:
            tmp = s[b]
            s[b] = s[a]
            s[a] = tmp
            a += 1
            b -= 1
        
