class Solution {
public:
    bool detectCapitalUse(string word) {
        int cC=0;
        for(char c:word){
            if(isupper(c)){
                cC++;
            }
        }
        if(cC==word.length()) return true;
        if(cC==0) return true;
        if(cC==1 && isupper(word[0])) return true; 
        return false;
    }
};