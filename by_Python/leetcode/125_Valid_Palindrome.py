class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert
        string = ""
        for x in s:
            if x.isalnum():
                string += x.lower()
        # check forward - backward
        if len(string) == 1:
            return True
        
        mid = len(string)//2
        forward = string[:mid]
        if len(string) % 2 == 1:
            backward = string[-1:mid:-1]
        else:
            backward = string[-1:mid-1:-1]
        
        return forward == backward