class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=[]
        m=max(candies)
        
        for i in range(len(candies)):
            v=candies[i]+extraCandies
            
            if v>=m:
                n.append(True)
            else:
                n.append(False)
        return n

        