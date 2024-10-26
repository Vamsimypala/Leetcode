class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=list(allowed)
        v=[]
        for i in words:
            for j in i:
                if j not in allowed:
                    v.append(i)
                    break
        print(v)
        print(words)
        return abs(len(words)-len(v))
                    
            
                
        