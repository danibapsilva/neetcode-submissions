class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            lookup = [0] * 26
            for ch in word:
                lookup[ord(ch) - ord('a')] += 1
            groups[tuple(lookup)].append(word)
        
        return list(groups.values())
