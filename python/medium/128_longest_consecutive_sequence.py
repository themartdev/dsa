from typing import List


class Sequence:
    def __init__(self, low: int, high: int):
        self.low = low
        self.high = high

    def get_length(self):
        return self.high - self.low + 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_by_low = {}
        seq_by_high = {}
        largest_seq = 0
        encountered = set()

        for num in nums:
            if num in encountered:
                continue
            encountered.add(num)

            if num + 1 in seq_by_low and num - 1 in seq_by_high:
                small_seq = seq_by_high[num - 1]
                large_seq = seq_by_low[num + 1]
                new_seq = Sequence(small_seq.low, large_seq.high)
                seq_by_low[new_seq.low] = new_seq
                seq_by_high[new_seq.high] = new_seq
                largest_seq = max(largest_seq, new_seq.get_length())
            elif num + 1 in seq_by_low:
                seq_by_low[num + 1].low = num
                seq_by_low[num] = seq_by_low[num + 1]
                largest_seq = max(largest_seq, seq_by_low[num].get_length())
            elif num - 1 in seq_by_high:
                seq_by_high[num - 1].high = num
                seq_by_high[num] = seq_by_high[num - 1]
                largest_seq = max(largest_seq, seq_by_high[num].get_length())
            else:
                new_seq = Sequence(num, num)
                seq_by_low[num] = new_seq
                seq_by_high[num] = new_seq
                largest_seq = max(largest_seq, new_seq.get_length())
        return largest_seq
