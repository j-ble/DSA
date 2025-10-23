class Solution:
    def simplifyPath(self, path: str) -> str:
        # using a stack data structure to store characters
        # since we are using a stack, this is going to be O(n) space complexity
        stack = []
        # we must have a string the stores the most recent directory
        cur = ""
        # we must go through every character within the input path & also add + '/' to insure one more loop
        for c in path + '/':
            # create a special case if c is == to '/'
            if c == '/':
                # if the current string has '..'
                if cur == '..':
                    # we are going to pop from the stack only if the stack is non-empty
                    if stack: stack.pop()
                # if the current string is not empty & current has '.'
                elif cur != "" and cur != '.':
                    # we append the current string to the stack
                    stack.append(cur)
                # once these conditions are met, we can reset the current string
                cur = ""
            # if we get a character that is not a '/'
            else:
                # we add that character to our current string
                cur += c
        # join the strings together with a '/' & start the string with a '/' & return the value
        return "/" + "/".join(stack)