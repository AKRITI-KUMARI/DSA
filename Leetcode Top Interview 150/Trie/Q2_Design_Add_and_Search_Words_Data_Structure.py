class Node:
    def __init__(self):
        self.children = [None] * 26
        self.eow = False 


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.eow = True

    def search(self, word: str) -> bool:
        return self._dfs(self.root, word, 0)

    def _dfs(self, curr: Node, word: str, i: int) -> bool:
        if curr is None:
            return False
        if i == len(word):
            return curr.eow

        c = word[i]
        if c == '.':
            # Try all possible children
            for child in curr.children:
                if child is not None and self._dfs(child, word, i + 1):
                    return True
            return False
        else:
            idx = ord(c) - ord('a')
            return self._dfs(curr.children[idx], word, i + 1)