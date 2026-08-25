class Solution:
    def longestPalindrome(self, s: str) -> int:
        unmatched = set()
        length = 0

        for ch in s:
            if ch in unmatched:
                unmatched.remove(ch)
                length += 2
            else:
                unmatched.add(ch)

        if unmatched:
            length += 1

        return length