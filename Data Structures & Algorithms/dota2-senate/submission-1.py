from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        R, D = deque(), deque()
        for indx, party in enumerate(senate):
            if party == 'R':
                R.append(indx)
            else:
                D.append(indx)
        
        while R and D:
            r, d = R.popleft(), D.popleft()
            if r < d:
                R.append(r + n)
            else:
                D.append(d + n)
        
        return "Radiant" if R else "Dire"