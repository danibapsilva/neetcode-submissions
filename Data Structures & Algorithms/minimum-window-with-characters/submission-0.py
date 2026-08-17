class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        m = len(s), len(t)

        freqT, freqS = {}, {}
        for ch in t:
            freqT[ch] = freqT.get(ch, 0) + 1

        have = l = 0
        res = ""
        for r, ch in enumerate(s):
            if ch in freqT:
                freqS[ch] = freqS.get(ch, 0) + 1
                if freqS[ch] <= freqT[ch]:
                    have += 1
            while have == len(t):
                curr = s[l: r + 1]
                if not res or len(res) > len(curr):
                    res = curr

                if s[l] in freqT:
                    freqS[s[l]] = freqS.get(s[l], 0) - 1
                    if freqS[s[l]] < freqT[s[l]]:
                        have -= 1
                l += 1
    
        return res
