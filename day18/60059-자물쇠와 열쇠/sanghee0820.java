import java.util.*;

// 12:30 - 1:10

// lock 빈 부분을 List에 저장.
// 왼쪽 위점을 기준으로, 0,0으로 저장.
// 회전 시 왼쪽위점은 고정.
// lock 빈 부분을 회전해가며 Key와 비교.

class Solution {
    public boolean solution(int[][] key, int[][] lock) {
        boolean answer = true;
        List<Position> pattern = new ArrayList<>();
        int leftTopRow = -1;
        int leftTopColumn = -1;
        for(int i = 0; i < lock.length; i++){
            for(int j = 0; j < lock[0].length; j++){
                if(lock[i][j] == 0){
                    if(leftTopRow == -1){
                        leftTopRow = i;
                        leftTopColumn = j;
                    }
                    pattern.add(new Position(i - leftTopRow,j - leftTopColumn));
                }
            }
        }
        
        for(int i = 0; i < 4; i++){
            for(int[] row : key){
                System.out.println(Arrays.toString(row));
            }
            System.out.println();
            if(checkPattern(pattern, key)){
                return true;
            }
            rotate(key);
        }
        return false;
    }
    
    public boolean checkPattern(List<Position> pattern, int[][] key){
        for(int i = 0; i < key.length; i++){
            for(int j = 0; j < key[0].length; j++){
                boolean flag = true;
                for(Position next: pattern){
                    int nextRow = i + next.row;
                    int nextColumn = j + next.column;
                    if((nextRow < 0 || nextRow > key.length - 1) || (nextColumn < 0 || nextColumn > key[0].length - 1)){
                        flag = false;
                        break;
                    }
                    if(key[nextRow][nextColumn] != 1){
                        flag = false;
                        break;
                    }
                }
                if(flag){
                    return true;
                }     
            }
        }
        return false;
    }
    
    public void rotate(int[][] matrix){
        int n = matrix.length;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = temp;
            }
        }
    }
    
    class Position{
        int row;
        int column;
        public Position(int row, int column){
            this.row = row;
            this.column = column;
        }

        
        public String toString(){
            return "Row : " + row + " Column : " + column;
        }
    }
}
