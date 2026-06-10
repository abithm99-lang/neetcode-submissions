class Solution {
    public int[][] dp;
    public int numDistinct(String s, String t) {
        dp = new int[s.length()][t.length()];
        for(int[] row: dp){
            Arrays.fill(row,-1);
        }
        return knapsack(0,0,s,t);
    }

    public int knapsack(int i, int j,String s, String t){
        if (j == t.length()) return 1; // Successfully matched all of t
        if (i == s.length()) return 0; // s is exhausted, no more subsequences possible

        if(dp[i][j]!=-1) return dp[i][j];
        
        if(s.charAt(i)==t.charAt(j)){
            dp[i][j] = knapsack(i+1,j+1,s,t) + knapsack(i+1,j,s,t);
        }else{
            dp[i][j] = knapsack(i+1,j,s,t);
        }

    return dp[i][j];
    }
}
