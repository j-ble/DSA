class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if not current_line:
                current_line.append(word)
                current_length = len(word)
            else:
                required = current_length + len(word) + len(current_line)
                if required <= maxWidth:
                    current_line.append(word)
                    current_length += len(word)
                else:
                    lines.append(current_line)
                    current_line = [word]
                    current_length = len(word)
        if current_line:
            lines.append(current_line)
        
        result = []
        for i in range(len(lines)):
            line = lines[i]
            if i == len(lines) - 1:
                s = ' '.join(line)
                s += ' ' * (maxWidth - len(s))
            elif len(line) == 1:
                s = line[0] + ' ' * (maxWidth - len(line[0]))
            else:
                sum_length = sum(len(word) for word in line)
                total_spaces = maxWidth - sum_length
                gaps = len(line) - 1
                space_between = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                s = ''
                for j in range(len(line)):
                    s += line[j]
                    if j < gaps:
                        spaces = space_between
                        if j < extra_spaces:
                            spaces += 1
                        s += ' ' * spaces
            result.append(s)
        
        return result
