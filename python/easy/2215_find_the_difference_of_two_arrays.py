class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set_1 = set(nums1)
        set_2 = set(nums2)

        out_1 = []
        out_2 = []
        for num in set_1:
            if num not in set_2:
                out_1.append(num)

        for num in set_2:
            if num not in set_1:
                out_2.append(num)

        return [out_1, out_2]
