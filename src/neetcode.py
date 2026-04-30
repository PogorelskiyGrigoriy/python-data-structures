from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_map = defaultdict(list)        
        for word in strs:
            key = tuple(sorted(Counter(word).items()))
            anagrams_map[key].append(word)
        return list(anagrams_map.values())