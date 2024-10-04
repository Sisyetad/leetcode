class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len=m+n
        left=m-1
        right=n-1
        for i in range(n+m-1,-1,-1):
            if((left!=-1) and(right!=-1) and (nums1[left]>=nums2[right])):
                nums1[i]=nums1[left]
                left-=1
            elif(right!=-1):
                nums1[i]=nums2[right]
                right-=1