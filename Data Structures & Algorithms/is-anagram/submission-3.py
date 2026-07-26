class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for ch in s:
            if ch not in t:
                return False
            t = t.replace(ch, "", 1)
        return True