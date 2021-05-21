from typing import List
class Solution:
    def findmedian(self,num:List[int])-> float:
        mid = len(num) // 2
        return (num[mid]+num[~mid])/2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int])-> float:
        #first we need to sort the arrays
        for x in nums2:
            nums1.append(x)
        merged = nums1
        list.sort(merged)
        return self.findmedian(merged)

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,2],[3,4]))