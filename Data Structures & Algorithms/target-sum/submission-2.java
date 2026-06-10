class Solution {
    public int length;
    public int[][] dp;

    public int findTargetSumWays(int[] nums, int target) {
        length = nums.length;
        int sum = 0;
        for (int val : nums) sum += val;

        // Validate if target is achievable
        if (sum - target < 0 || (sum - target) % 2 == 1) return 0;

        int subsetSumTarget = (sum - target) / 2;

        // Initialize dp array with subsetSumTarget size
        dp = new int[length][subsetSumTarget + 1];
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        return knapsack(length - 1, subsetSumTarget, nums);
    }

    public int knapsack(int idx, int target, int[] nums) {
        // Base case
        if (idx == 0) {
            if (target == 0 && nums[0] == 0) return 2; // Two ways: +0 or -0
            if (target == 0 || target == nums[0]) return 1; // One way
            return 0;
        }

        // Memoization
        if (dp[idx][target] != -1) return dp[idx][target];

        // Recursive cases
        int notPick = knapsack(idx - 1, target, nums);

        int pick = 0;
        if (target >= nums[idx]) pick = knapsack(idx - 1, target - nums[idx], nums);

        dp[idx][target] = pick + notPick;

        return dp[idx][target];
    }
}



// class Solution {
//     public int length;
//     public int[][] dp;
//     public int offset;
//     public int findTargetSumWays(int[] nums, int target) {
//         length = nums.length;

//         int sum=0;
//         for(int sum1: nums) sum+=sum1;

//         if (Math.abs(target) > sum) return 0;
//         offset = sum;
//         dp = new int[length][2*sum+1];

//         for(int[] row: dp){
//             Arrays.fill(row,-1);
//         }

//         return knapsack(0,0,target,nums);
//     }

//     public int knapsack(int idx, int curSum, int target,int[] nums){
//         if(idx==length){
//             return curSum==target ? 1:0;
//         }
//         int mapSum = curSum + offset;
//         if(dp[idx][mapSum]!=-1) return dp[idx][mapSum];

//         int pickAdd = knapsack(idx + 1, curSum + nums[idx], target, nums);
//         int pickSubtract = knapsack(idx + 1, curSum - nums[idx], target, nums);

//         dp[idx][mapSum]= pickAdd + pickSubtract;

//     return dp[idx][mapSum]; 
//     }
// }
