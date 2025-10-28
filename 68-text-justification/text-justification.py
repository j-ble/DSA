class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # we need to pack the words into lines with exaclty maxWidth characters 
        res = []
        i = 0
        # we need to process all words
        while i < len(words):
            # we need to find how many words fit into current line
            lineWords = []
            lineLength = 0
            # we iterate through words, pack greedily into lines
            while i < len(words):
                # we check if adding next word would exceed maxWidth
                # we need at least 1 space between each word
                if lineLength + len(words[i]) + len(lineWords) > maxWidth:
                    break
                lineWords.append(words[i])
                lineLength += len(words[i])
                i += 1
            # we build the line with proper spacing 
            # if last line or single word, left-justified
            if i == len(words) or len(lineWords) == 1:
                line = ' '.join(lineWords)
                line += ' ' * (maxWidth - len(line))
            else:
                # we need to distribute spaces evenly 
                totalSpaces = maxWidth - lineLength
                gaps = len(lineWords) - 1
                spacesPerGap = totalSpaces // gaps
                extraSpaces = totalSpaces % gaps
                # we build line with distributed spaces
                line = ""
                for j, word in enumerate(lineWords):
                    line += word
                    if j < gaps:
                        # we must add base spaces plus 1 extra for leftmost gaps 
                        line += ' ' * (spacesPerGap + (1 if j < extraSpaces else 0))
            res.append(line)
        return res
# Time Complexity O(n) where n is total chars in all words
# Space Complexity O(n) for the res array