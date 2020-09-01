class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        c = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                c.append(nums1[i])
                i += 1
            else:
                c.append(nums2[j])
                j += 1

        while i < m:
            c.append(nums1[i])
            i += 1

        while j < n:
            c.append(nums2[j])
            j += 1

        for i in range(m + n):
            nums1[i] = c[i]
