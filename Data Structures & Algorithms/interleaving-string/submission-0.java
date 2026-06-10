class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int length = s1.length() + s2.length();
        int s3length = s3.length();
        if(length != s3length){
            return false;
        }
        if(s3length==0 && length==0) return true;
        return knapsack(s1,s2,s3);
    }

    public boolean knapsack(String t1,String t2,String combined){
        if(combined.isEmpty()){
            return t1.isEmpty() && t2.isEmpty();
        }

        if(t2.isEmpty()){
            return combined.equals(t1);
        }

        if (t1.isEmpty()) {
            return t2.equals(combined);
        }
        
        //String in both s1 and s2
        if(combined.charAt(0)==t1.charAt(0) && combined.charAt(0)==t2.charAt(0)){
            return knapsack(t1.substring(1), t2, combined.substring(1)) 
           || knapsack(t1, t2.substring(1), combined.substring(1));
        }else if(combined.charAt(0)==t1.charAt(0)){//String in s1 
            return knapsack(t1.substring(1),t2,combined.substring(1));
        }else{ //String in s2
            return knapsack(t1,t2.substring(1),combined.substring(1));
        }

    }
}
