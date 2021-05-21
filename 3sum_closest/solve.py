from typing import List
class Solution:
    def threeSumClosest(self,num:List[int],target:int) -> int:
        num = sorted(num) # sort the given list
        i = 0
        closest = float('inf')
        for i in range(len(num)-2):
            l = i + 1
            r = len(num) - 1
            while l < r :
                s = num[i] + num[l] + num[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return target
                if abs(target-closest) > abs(target-s):
                    closest = s
        return closest       
if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([1,1,1],3))