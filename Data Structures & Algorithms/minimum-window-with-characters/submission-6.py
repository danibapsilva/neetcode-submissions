class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freqT, freqWindow = {}, {}
        for ch in t:
            freqT[ch] = freqT.get(ch, 0) + 1

        have = l = 0
        res = ""
        for r, ch in enumerate(s):
            freqWindow[ch] = freqWindow.get(ch, 0) + 1
            if ch in freqT and freqWindow[ch] <= freqT[ch]:
                have += 1
            while have == len(t):
                curr = s[l: r + 1]
                if not res or len(res) > len(curr):
                    res = curr

                freqWindow[s[l]] -= 1
                if s[l] in freqT and freqWindow[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1
    
        return res
