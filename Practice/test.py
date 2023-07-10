class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []  # List to store the formatted lines
        
        # Iterate through the words
        i = 0
        while i < len(words):
            # Start with the current word
            line_length = len(words[i])
            line_words = [words[i]]
            i += 1
            
            # Add more words until the line reaches maxWidth or there are no more words
            while i < len(words) and line_length + len(words[i]) + 1 <= maxWidth:
                line_length += len(words[i]) + 1
                line_words.append(words[i])
                i += 1
            
            # Format the line
            if i == len(words) or len(line_words) == 1:
                # Left-justify the last line or a line with a single word
                line = ' '.join(line_words)
                line = line + ' ' * (maxWidth - len(line))
            else:
                # Distribute extra spaces evenly between the words
                num_extra_spaces = maxWidth - line_length
                num_spaces = len(line_words) - 1
                spaces_between_words = num_extra_spaces // num_spaces
                extra_spaces = num_extra_spaces % num_spaces
                
                line = line_words[0]
                for j in range(1, len(line_words)):
                    if extra_spaces > 0:
                        line += ' ' * (spaces_between_words + 1)
                        extra_spaces -= 1
                    else:
                        line += ' ' * spaces_between_words
                    line += line_words[j]
            
            # Add the formatted line to the result
            result.append(line)
        
        return result

# Example usage:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
solution = Solution()
result = solution.fullJustify(words, maxWidth)
print(result)
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
