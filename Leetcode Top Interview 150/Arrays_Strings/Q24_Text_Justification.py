class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def findRight(left):
            right = left
            sum = len(words[right])
            right += 1
            while (right < len(words) and (sum + 1 + len(words[right])) <= maxWidth):
                sum += 1 + len(words[right])
                right += 1
            return right - 1

        def justify(left, right):
            if right - left == 0:
                return padResult(words[left])
            if right == len(words)-1:
                isLastLine = True
            else:
                isLastLine = False
            numSpaces = right - left
            totalSpace = maxWidth - wordsLength(left, right)
            if isLastLine:
                space = " "
                remainder = 0
            else:
                space = blank(totalSpace // numSpaces)
                remainder = totalSpace % numSpaces
            result = ""
            for i in range(left, right+1):
                result += words[i] + space
                if remainder > 0:
                    result += " "
                remainder -= 1
            return padResult(result.strip())
        
        def wordsLength(left, right):
            wordsLength = 0
            for i in range(left, right+1):
                wordsLength += len(words[i])
            return wordsLength
        
        def padResult(result):
            return result + blank(maxWidth - len(result))

        def blank(length):
            return ' '*length

        ans = []
        left = 0
        while left < len(words):
            right = findRight(left)
            ans.append(justify(left, right))
            left = right + 1
        return ans