class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        VOWELS = set("aeiou")

        prefix = [0] * len(words)
        for indx, word in enumerate(words):
            if not indx and word[0] in VOWELS and word[-1] in VOWELS:
                prefix[indx] = 1
            elif word[0] in VOWELS and word[-1] in VOWELS:
                prefix[indx] = prefix[indx - 1] + 1
            else:
                prefix[indx] = prefix[indx - 1]
    
        res = []
        for low, high in queries:
            if not low:
                count = prefix[high]
            else:
                count = prefix[high] - prefix[low - 1]
            res.append(count)
        
        return res