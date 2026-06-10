class Solution {
    public int[][] dp;
    public int longestIncreasingPath(int[][] matrix) {
        int maxLength = 0;
        dp = new int[matrix.length][matrix[0].length];
        for(int[] row: dp){
            Arrays.fill(row,-1);
        }
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                if(dp[i][j]==-1){
                   dfs(i,j,matrix);    
                }
                maxLength = Math.max(maxLength, dp[i][j]);
            }
        }

    return maxLength;
    }

    public int dfs(int i,int j,int[][] matrix){
        // if(i<0 || j<0 || i>=matrix.length || j>=matrix[0].length) return 0;
        if(dp[i][j]!=-1) return dp[i][j];
        int[] row = {1,0,-1,0};
        int[] col = {0,1,0,-1};
        dp[i][j] = 1; 
        for(int val=0;val<4;val++){
            int newRow = i + row[val];
            int newCol = j + col[val];
            if (newRow >= 0 && newRow < matrix.length && newCol >= 0 && newCol < matrix[0].length 
                && matrix[i][j] < matrix[newRow][newCol]) {
                    // dp[i][j] = 1;
                    // dp[i][j] = Math.max(dp[i][j],dfs(i+row[val],j+col[val],matrix));
                    dp[i][j] = Math.max(dp[i][j], 1 + dfs(newRow, newCol, matrix));
            }
        }
    return dp[i][j];
    }
}
