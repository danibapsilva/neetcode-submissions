class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res = []
        line = ""

        for word in words:
            if len(line) + len(word) <= maxWidth:
                line += word + ' '
                continue

            line = line.strip()
            splitLine = line.split(' ')

            spaceCount = len(splitLine) - 1
            wordLen = sum(len(w) for w in splitLine)

            # One word in the line
            if spaceCount == 0:
                res.append(line + ' ' * (maxWidth - len(line)))
                line = word + ' '
                continue

            totalSpaces = maxWidth - wordLen
            spacePad = totalSpaces // spaceCount
            extra = totalSpaces % spaceCount

            newLine = ""

            for i, w in enumerate(splitLine):
                newLine += w

                if i < spaceCount:
                    spaces = spacePad
                    if i < extra:
                        spaces += 1

                    newLine += ' ' * spaces

            res.append(newLine)
            line = word + ' '

        # Last line
        line = line.strip()
        line += ' ' * (maxWidth - len(line))
        res.append(line)

        return res