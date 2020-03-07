class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums3 = []
        
        while nums1 or nums2:
            if nums1 and nums2: # both lists have elements
                nums3 += [nums1.pop()] if nums1[-1] > nums2[-1] else [nums2.pop()]
            elif nums1: # nums2 is empty but nums1 has elements
                nums3 += [nums1.pop()]
            else: # nums1 is empty but nums2 has elements
                nums3 += [nums2.pop()]
        
        length = len(nums3) 

        # to determine if the length of nums1 is odd or even
        odd = False if length % 2 == 0 else True
        midpoint = length // 2 - 1
        
        # if odd return median
        # if even return average of the medians
        return nums3[midpoint+1] if odd else (nums3[midpoint] + nums3[midpoint+1]) / 2