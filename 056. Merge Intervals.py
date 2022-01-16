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

    
class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> ans = new ArrayList<>();
        Arrays.sort(intervals, (o1, o2) -> o1[0] == o2[0] ? o1[1] - o2[1] : o1[0] - o2[0]);
        int start = intervals[0][0], end = intervals[0][1];
        for (int i = 1; i < intervals.length; i++){
            if (intervals[i][0] <= end){//两个区间有重叠
                end = Math.max(end, intervals[i][1]);
            }else{
            	//两个区间没有重叠，保存[start,end]，然后更新
                ans.add(new int[] {start, end});
                start = intervals[i][0];
                end = intervals[i][1];
            }
        }
        ans.add(new int[] {start, end});
        int[][] res = new int[ans.size()][2];
        for (int i = 0; i < res.length; i++){
            res[i] = ans.get(i);
        }
        return res;
    }
}
