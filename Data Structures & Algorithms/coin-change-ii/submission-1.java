class Solution {
    public int[][] dp;
    public int change(int amount, int[] coins) {
        if(coins.length==0 && amount>0){
            return 0;
        }
        if(coins.length>0 && amount==0){
            return 1;
        }
        dp = new int[coins.length][amount+1];
        for(int[] row : dp){
            Arrays.fill(row,-1);
        }
        knapsack(coins.length-1,amount,coins);
    return dp[coins.length-1][amount];
    }

    public int knapsack(int idx, int amount,int[] coins){
        if(amount==0) return 1;
        if(idx<0 || amount<0) return 0;

        if(dp[idx][amount]!=-1) return dp[idx][amount];

        int notPick = knapsack(idx-1,amount,coins);

        int pick = 0;
        if(amount >= coins[idx]){
            pick = knapsack(idx,amount-coins[idx],coins);
        }

        dp[idx][amount]= pick + notPick;

    return dp[idx][amount]; 
    }
}
