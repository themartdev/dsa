class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        reg = {}
        operations = 0
        for num in nums:
            complement = k - num
            if complement in reg and reg[complement] > 0:
                reg[complement] -= 1
                operations += 1
            else:
                if num not in reg:
                    reg[num] = 0
                reg[num] += 1
