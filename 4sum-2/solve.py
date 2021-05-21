from typing import List
from collections import Counter
class Solution:
    def fourSumCount(self,n1:List[int],n2:List[int],n3:List[int],n4:List[int]) -> int:
        sums = Counter(k + l for k in n3 for l in n4)
        return sum(sums.get(-(i+j),0) for i in n1 for j in n2)
if __name__ == "__main__":
    s = Solution()
    print(s.fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))
    # s.fourSumCount([1,2],[-2,-1],[-1,2],[0,2])