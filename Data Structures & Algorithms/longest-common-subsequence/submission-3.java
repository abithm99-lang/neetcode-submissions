class Solution {
    public int[][] dp;
    public int longestCommonSubsequence(String text1, String text2) {
        int lengthA = text1.length();
        int lengthB = text2.length();
        
        dp = new int[lengthA][lengthB];
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        // Call knapsack function with proper indices
    return knapsack(lengthA - 1, lengthB - 1, text1, text2);
    }

    public int knapsack(int i, int j,String text1, String text2){
        if(i<0 || j<0) return 0;

        if(dp[i][j]!=-1) return dp[i][j];

        //same
        if(text1.charAt(i)==text2.charAt(j)){
            dp[i][j] = 1 + knapsack(i-1,j-1,text1,text2); 
        }else{
            //notSame
            dp[i][j] = Math.max(knapsack(i-1,j,text1,text2),knapsack(i,j-1,text1,text2));
        }
        
        
        

    return dp[i][j]; 
    }
}
