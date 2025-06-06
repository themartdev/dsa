from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(position[i], speed[i]) for i in range(len(position))]
        input = sorted(combined, key=lambda x: x[0], reverse=True)
        stack: list[float] = []
        for pos, spd in input:
            ttl = (target - pos) / spd
            print(f"pos {pos}, spd {spd}, ttl {ttl}")
            if not stack:
                stack.append(ttl)
            elif ttl <= stack[-1]:
                pass
            else:
                stack.append(ttl)

        return len(stack)
