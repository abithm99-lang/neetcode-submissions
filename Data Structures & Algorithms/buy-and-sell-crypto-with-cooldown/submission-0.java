class Solution {
    public int maxProfit(int[] prices) {
        return knapsack(0,1,prices);
    }

    public int knapsack(int idx, int buysell, int[] prices){
        if(idx==prices.length) return 0;

        int profit = 0;

        if(buysell == 1){
            profit = Math.max(-1*prices[idx] + knapsack(idx+1,0,prices), 0 + knapsack(idx+1,1,prices));
        }else{
            // profit = Math.max(prices[idx] + knapsack(idx+2,1,prices), 0 + knapsack(idx+1,0,prices));

            profit = prices[idx];
            if((idx+2)<prices.length){
                profit += knapsack(idx+2,1,prices);
            }

            profit = Math.max(profit,0 + knapsack(idx+1,0,prices));
        }

    return profit;
    }
}
