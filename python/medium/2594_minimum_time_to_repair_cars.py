class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        repairs = [0 for _ in ranks]
        for _ in range(cars):
            best_time, best_idx = float("inf"), -1
            for i in range(len(repairs)):
                new_total = ((repairs[i] + 1) ** 2) * ranks[i]
                if new_total < best_time:
                    best_time = new_total
                    best_idx = i
            repairs[best_idx] += 1

        max_val = 0
        for i in range(len(repairs)):
            val = (repairs[i] ** 2) * ranks[i]
            max_val = max(max_val, val)
        return max_val
