class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        
        res = []
        intervals.sort()
        
        for i in range(len(intervals)):
            
            if i == len(intervals)-1:
                res.append(intervals[i])
                break
                
            if intervals[i][1] < intervals[i+1][0]:
                res.append(intervals[i])
            
            else:
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])    
                
        return res 
