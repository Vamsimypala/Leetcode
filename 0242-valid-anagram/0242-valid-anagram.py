class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=0
        v=[]
        b,k=list(set(s)),list(set(t))
        if len(s)==len(t):
            for i in b:
                if s.count(i)==t.count(i):
                    c+=1
            return True if c==len(b) and c==len(k) else False
        else:
            return False
        
        

            
        