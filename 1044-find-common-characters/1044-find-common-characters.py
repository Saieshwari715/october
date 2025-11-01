class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s=list(words[0])
        for i in words[1:]:
            a=[]
            for j in i:
                if j in s:
                    a.append(j)
                    s.remove(j)
            s=a
        return s
        