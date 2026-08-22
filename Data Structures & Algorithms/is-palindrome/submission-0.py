class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""
        for i in range(len(s)):
            if s[i].isalnum():
                cleaned+=s[i].lower()

        for i in range(len(cleaned)):
            if cleaned[i] != cleaned[len(cleaned)-i-1]:
                return False
        return True
        