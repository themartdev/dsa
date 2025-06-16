class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        enc = set()

        for num in nums:
            if num in enc:
                enc.remove(num)
            else:
                enc.add(num)

        for elem in enc:
            return elem
