from typing import List
class Solution:
  def combinationSum(self,c:List[int],t:int) -> List[List[int]]:
    self.sol=list()
    self.backtrack(t,list(),0,c)
    return self.sol
  def backtrack(self,remain,curr,start,cands):
    if remain == 0:
      self.sol.append(list(curr))
    if remain > 0:
      for i in range(start,len(cands)):
        curr.append(cands[i])
        self.backtrack(remain-cands[i],curr,i,cands)
        curr.pop()
if __name__ == "__main__":
  s = Solution()
  print(s.combinationSum([10,1,2,7,6,1,5],8))
  print(s.combinationSum([2,3,6,7],7))
  print(s.combinationSum([2,3,5],8))
