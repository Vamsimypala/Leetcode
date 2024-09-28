class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        m=len(word)
        if word.isupper():
            return True
        c=0
        b=0
        for i in word :
            if i.isupper():
                c+=1
            else:
                b+=1
        if word[0].isupper() and c==1:
            return True
        elif b==m:
            return True
        else:
            return False
            
                
            
            

        