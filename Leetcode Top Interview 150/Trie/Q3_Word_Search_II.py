class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None  # store word at leaf

class Solution:
    def buildTrie(self, words: List[str]) -> TrieNode:
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                idx = ord(c) - ord('a')
                if not node.children[idx]:
                    node.children[idx] = TrieNode()
                node = node.children[idx]
            node.word = w
        return root

    def dfs(self, board: List[List[str]], i: int, j: int, node: TrieNode, result: Set[str]):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        c = board[i][j]
        if c == '#' or not node.children[ord(c) - ord('a')]:
            return

        node = node.children[ord(c) - ord('a')]
        if node.word:
            result.add(node.word)
            node.word = None  # avoid duplicates

        board[i][j] = '#'  # mark visited
        self.dfs(board, i + 1, j, node, result)
        self.dfs(board, i - 1, j, node, result)
        self.dfs(board, i, j + 1, node, result)
        self.dfs(board, i, j - 1, node, result)
        board[i][j] = c  # restore

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.buildTrie(words)
        result = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, result)

        return list(result)
  