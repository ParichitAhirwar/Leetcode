class Solution:
    def compress(self, chars: List[str]) -> int:
        w=0
        i=0
        while i<len(chars):
            ch=chars[i]
            c=0
            while i<len(chars) and ch==chars[i]:
                i+=1
                c+=1
            chars[w]=ch
            w+=1
            if c>1:
                for j in str(c):
                    chars[w]=j
                    w+=1
        return w