import java.util.*;
// 시간초과 / 68점
// BFS -> 그전이랑 같은 방향이면 Cost + 100 / 아니면 Cost + 500
class Solution {
    private static final int[][] directions = {{0,1}, {1,0}, {-1, 0}, {0, -1}};
    public int solution(int[][] board) {
        int answer = BFS(board);
        return answer;
    }
    
    public int BFS(int[][] board){
        Queue<List<List<Integer>>> queue = new LinkedList<>();
        // row, column / direction / cost
        queue.add(List.of(List.of(0,0, -1, 0)));
        
        int totalCost = Integer.MAX_VALUE;
        
        while(!queue.isEmpty()){
            List<List<Integer>> path = queue.poll();
            List<Integer> current = path.get(path.size() - 1);
            
            if( (current.get(0) == board.length - 1) && (current.get(1) == board.length - 1) ){
                totalCost = Math.min(totalCost, current.get(3));
                continue;
            }
            
            for(int i = 0; i < 4; i++){
                int cost = 0;
                if( (current.get(2) == -1) || (current.get(2) == i)){
                    cost = 100;
                }else{
                    cost = 600;
                }
                
                List<Integer> next = new ArrayList<>(Arrays.asList(
                    current.get(0) + directions[i][0], current.get(1) + directions[i][1]
                    , i, current.get(3) + cost));
                
                if( (0 <= next.get(0) && next.get(0) < board.length) 
                         && (0 <= next.get(1) && next.get(1) < board.length)
                        && !pathContains(path, next) && board[next.get(0)][next.get(1)] != 1 && next.get(3) < totalCost ){
                    List<List<Integer>> newPath = new ArrayList<>(path);
                    newPath.add(next);
                    queue.add(newPath);
                }
            }
        }
        return totalCost;
    }
    
    private boolean pathContains(List<List<Integer>> path, List<Integer> next) {
        for (List<Integer> p : path) {
            if (p.get(0).equals(next.get(0)) && p.get(1).equals(next.get(1))) {
                return true;
            }
        }
    return false;
}
}
