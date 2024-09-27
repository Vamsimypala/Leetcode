class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s=list(s)
        
        v=""
        for i in range(len(s)):
            v+=s[-1]
            s.pop()
            s.insert(0,v)
            v=""
            print(s)
            m="".join(s)
            if m==goal:
                return True
        else:
            return False
        
            
            
            
            
            
        