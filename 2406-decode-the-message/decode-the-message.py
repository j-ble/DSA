class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # we need a mapping from cipher letters to alphabet letters
        mapping = {}
        # we build substitution table from key's first appearance of each letter 
        # we track which alphabet letter to assign next
        alphabet_i = 0
        # we go thorugh key to build the substitution table
        for char in key:
            # we skip spaces
            if char == ' ':
                continue
            # only map letters we havn't seen before
            if char not in mapping:
                # map cipher letter to current alphabet letter
                mapping[char] = chr(ord('a') + alphabet_i)
                # we move to the next alphabet letter
                alphabet_i += 1
        # then we decode message using the mapping
        res = []
        for char in message:
            # spaces remain spaces
            if char == ' ':
                res.append(' ')
            else:
                # we substitute using the mapping 
                res.append(mapping[char])
        # join and return decoded message
        return ''.join(res)
# Time Complexity is O(n + m) where n is length of key, and m is length of message
# Space Complexity is O(1) since mapping is at most 26 letters
