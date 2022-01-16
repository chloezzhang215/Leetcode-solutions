class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitLog = []
        letterLog = []
        for s in logs:
            if s.split(" ")[1][0].isdigit():
                digitLog.append(s)
            if s.split(" ")[1][0].isalpha():
                letterLog.append(s)
        letterLog = sorted(letterLog,key=lambda s:s.split(" ")[0])
        letterLog = sorted(letterLog,key=lambda s:" ".join(s.split(" ")[1:]))
        logs = letterLog + digitLog 
        return logs
