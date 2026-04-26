from sortedcontainers import SortedList

class Words:
    def __init__(self):
        self._data = SortedList(key=str.lower)

    def add_word(self, word: str):
        index = self._data.bisect_left(word)
        
        if index < len(self._data) and self._data[index].lower() == word.lower():
            raise ValueError("Word already exists")
        
        self._data.add(word)
        
    def words_starts_with(self, prefix: str) -> list[str]:
        prefix = prefix.lower()
        result = []
        
        # Find the starting index for the prefix O(log n)
        idx = self._data.bisect_left(prefix)
        
        # Iterate and collect matching words
        for i in range(idx, len(self._data)):
            word = self._data[i]
            if word.lower().startswith(prefix):
                result.append(word)
            else:
                break
                
        return result