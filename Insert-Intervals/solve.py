from bisect import insort
from typing import List
class Solution:
  def insert(self,intervals:List[List[int]],newInterval:List[int]) -> List[List[int]]:
    intervals.sort(key = lambda x:x[0])
    insort(intervals,newInterval)
    start = 0
    end = len(intervals) - 1
    while (start< end):
      if((intervals[start][1] >= intervals[start+1][0]) and (intervals[start][0] <=intervals[start][1])):
        intervals[start][1] = max(intervals[start][1],intervals[start+1][1])
        del intervals[start + 1]
        end -= 1
      else:
        start += 1
    return intervals
if __name__ == "__main__":
  s = Solution()
  print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
  print(s.insert([],[5,7]))
  print(s.insert([[1,5]],[2,3]))
  print(s.insert([[1,5]],[2,7]))
