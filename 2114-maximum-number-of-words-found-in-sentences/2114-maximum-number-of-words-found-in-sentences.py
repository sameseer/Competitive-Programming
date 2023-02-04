class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for i in sentences:
            if len(i.split()) > count:
                count = len(i.split())
        return count