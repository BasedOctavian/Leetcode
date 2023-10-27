class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # End goal is to merge nums 1 & 2 into the array of nums 1 with an increasing order
        
        # Initialize three pointers used to hold array indexing
        p1, p2, p = m - 1, n - 1, m + n - 1

        # Start a loop that runs when both p1 and p2 are still being traversed
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                # Place the larger element at the end of nums1
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

        # If there are remaining elements in nums1, copy them to the beginning of nums1
        while p1 >= 0:
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1
