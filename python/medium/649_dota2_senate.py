class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = [x for x in senate]
        n = len(senate)
        nr, nd = 0, 0
        for p in senate:
            if p == "R":
                nr += 1
            elif p == "D":
                nd += 1

        i, del_d, del_r = 0, 0, 0
        while 1:
            p = senate[i % n]
            print(f"i={i}, p={p}, senate={senate}")
            if p == "R":
                if del_r > 0:
                    senate[i % n] = "silenced"
                    del_r -= 1
                    nr -= 1
                else:
                    if nd == 0:
                        return "Radiant"
                    else:
                        del_d += 1

            elif p == "D":
                if del_d > 0:
                    senate[i % n] = "silenced"
                    del_d -= 1
                    nd -= 1
                else:
                    if nr == 0:
                        return "Dire"
                    else:
                        del_r += 1

            i += 1
