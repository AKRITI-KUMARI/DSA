class Trie:
    class Node:
        def __init__(self):
            self.children = [None]*26
            self.eow = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for level in range(len(word)):
            idx = ord(word[level]) - ord('a')
            if curr.children[idx] == None:
                curr.children[idx] = self.Node()
            curr = curr.children[idx]
        curr.eow = True
    
    def search(self, word: str) -> bool:
        curr = self.root
        for level in range(len(word)):
            idx = ord(word[level]) - ord('a')
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return curr.eow

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for level in range(len(prefix)):
            idx = ord(prefix[level]) - ord('a')
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)