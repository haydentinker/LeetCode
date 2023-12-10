class Solution {
    public int[][] transpose(int[][] matrix) {
        int[][] result = new int[matrix[0].length][matrix.length];
        for(int i=0;i<matrix[0].length;i++){
            int[] newRow = new int[matrix.length];
            for(int j=0;j<matrix.length;j++){
                newRow[j]=matrix[j][i];
                
            }
            result[i]=newRow;
        }
        return result;
    }
}