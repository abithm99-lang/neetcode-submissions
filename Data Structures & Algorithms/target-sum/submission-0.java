class Solution {
    public int length;
    public int[][] dp;
    public int offset;
    public int findTargetSumWays(int[] nums, int target) {
        length = nums.length;

        int sum=0;
        for(int sum1: nums) sum+=sum1;

        if (Math.abs(target) > sum) return 0;
        offset = sum;
        dp = new int[length][2*sum+1];

        for(int[] row: dp){
            Arrays.fill(row,-1);
        }

        return knapsack(0,0,target,nums);
    }

    public int knapsack(int idx, int curSum, int target,int[] nums){
        if(idx==length){
            return curSum==target ? 1:0;
        }
        int mapSum = curSum + offset;
        if(dp[idx][mapSum]!=-1) return dp[idx][mapSum];

        int pickAdd = knapsack(idx + 1, curSum + nums[idx], target, nums);
        int pickSubtract = knapsack(idx + 1, curSum - nums[idx], target, nums);

        dp[idx][mapSum]= pickAdd + pickSubtract;

    return dp[idx][mapSum]; 
    }
}
