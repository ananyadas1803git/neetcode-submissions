class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [ch.lower() for ch in s if ch.isalnum()]#here we convert strings into alphanumeric characters to check character by character
        #eg. ["Hello"]--> ["H","e","l","l","o"]
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False



        