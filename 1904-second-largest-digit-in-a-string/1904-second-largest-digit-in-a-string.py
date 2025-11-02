class Solution:
    def secondHighest(self, s: str) -> int:
        n=set()
        num=set("0123456789")
        for i in s:
            if i in num:
                n.add(i)
        n=sorted(n)
        if len(n)>=2:
            return int(n[-2])
        else:
            return -1

        