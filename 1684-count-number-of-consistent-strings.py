class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = [s for s in allowed]
        print(allowed)

        consistent = len(words)
        for word in words:
            for w in word:
                if w not in allowed:
                    consistent += -1
                    break

        return consistent
