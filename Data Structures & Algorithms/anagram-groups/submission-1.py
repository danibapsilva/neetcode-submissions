class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic: {List[int]: List[str]} = {}
        result = []
        for i, s in enumerate(strs):
            lookup = [0] * 26
            for i in range(len(s)):
                lookup[ord(s[i]) - ord('a')] += 1
            
            dic.setdefault(tuple(lookup), []).append(s)
        return list(dic.values())