class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def fun(x):
            s=str(x)
            for i in set(s):
                if(s.count(i)!=int(i)):
                    return False
            return True
        n=n+1
        while True:
            if(fun(n)):
                return n
            n+=1