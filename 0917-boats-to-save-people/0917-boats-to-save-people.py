class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        b=0
        people.sort()
        i,j=0,len(people)-1
        while i<=j:
            if(people[i]+people[j]<=limit):
                i+=1
            j-=1
            b+=1
        return b
           
           