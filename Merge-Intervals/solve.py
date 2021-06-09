from typing import List
class Solution:
  def merge(self,intervals:List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x:x[0])
    print(intervals)
    start = 0
    end = len(intervals) - 1
    while (start<end):
      if((intervals[start][1] >= intervals[start+1][0]) and (intervals[start][0] <= intervals[start][1])):
        intervals[start][1] =max(intervals[start][1],intervals[start+1][1]) 
        del intervals[start+1]
        end-=1
      else:
        start+=1
    return intervals
if __name__ == "__main__":
  s = Solution()
  print(s.merge([[0,0],[0,0]]))
  print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
  print(s.merge([[1,4],[4,5]]))
  print(s.merge([[5,7],[8,11]]))
  print(s.merge([[6,8],[1,9],[2,4],[4,7]]))
