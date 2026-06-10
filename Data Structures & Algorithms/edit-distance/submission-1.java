class Solution {
    public int[][] dp;
    public int minDistance(String word1, String word2) {
        dp = new int[word1.length() + 1][word2.length() + 1];
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }
    return knapsack(0,0,word1,word2);
    }

    public int knapsack(int i,int j,String s1, String s2){
        //base case
        if (i == s1.length()) return s2.length() - j; // Insert the remaining characters of s2
        if (j == s2.length()) return s1.length() - i; // Delete the remaining characters of s1

        int val = 0;
        if(s1.charAt(i)==s2.charAt(j)){
            val = knapsack(i+1,j+1,s1,s2);
        }else{
            val = Math.min(knapsack(i,j+1,s1,s2),knapsack(i+1,j,s1,s2));//insert,delete
            val = Math.min(val,knapsack(i+1,j+1,s1,s2));//replace
            val+=1;
        }
    return val;
    }
}
