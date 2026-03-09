class Solution {
public:
    int numberOfStableArrays(int z, int o, int l) {
        const int MOD=1e9+7;
        vector<vector<vector<long long>>> dp(
            z+1,vector<vector<long long>>(o+1,vector<long long>(2,0))
        );
        for(int i=1;i<=min(l,z);i++) dp[i][0][0]=1;
        for(int j=1;j<=min(l,o);j++) dp[0][j][1] = 1;
        for(int i=1;i<=z;i++){
            for(int j=1;j<=o;j++){
                long long x=(i-l-1>=0) ? dp[i-l-1][j][1]:0;
                long long y=(j-l-1>=0) ? dp[i][j-l-1][0]:0;
                dp[i][j][0]=
                    (dp[i-1][j][0]+dp[i-1][j][1]-x+MOD)%MOD;
                dp[i][j][1]=
                    (dp[i][j-1][0]+dp[i][j-1][1]-y+MOD)%MOD;
            }
        }
        return (dp[z][o][0]+dp[z][o][1])%MOD;
    }
};