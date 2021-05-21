from typing import List
class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    self.output = list()
    self.backtrack(target,list(),0,sorted(candidates))
    return self.output
  def backtrack(self,remain,curr,start,cands):
    if remain  == 0:
      self.output.append(list(curr))
    for i in range(start,len(cands)):
      if cands[i] > remain:
        break
      if i != start and cands[i] == cands[i-1]:
        continue
      curr.append(cands[i])
      self.backtrack(remain-cands[i],curr,i+1,cands)
      curr.pop()

if __name__ == "__main__":
  s = Solution()
  print(s.combinationSum2([10,1,2,7,6,1,5],8))
  print(s.combinationSum2([2,5,2,1,2],5))
  print(s.combinationSum2([1],2))

