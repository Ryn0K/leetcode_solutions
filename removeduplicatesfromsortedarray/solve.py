from typing import List
class Solution:
    def removeDuplicates(self,nums:List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        i = 0
        while (i < (len(nums)-1)):
            if nums[i] == nums[i+1]: # checking if the character after current element are equal
                del nums[i]
            else:
                i += 1
        return len(nums)
if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,2]))