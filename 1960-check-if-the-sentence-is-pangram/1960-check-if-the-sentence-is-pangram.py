class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=set(sentence)
        a=set("abcdefghijklmnopqrstuvwxyz")
        if(len(s)==len(a)):
            return True
        return False
        