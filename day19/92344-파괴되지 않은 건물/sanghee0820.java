import java.util.*;
class Solution {
    public int solution(int[][] board, int[][] skills) {
        int answer = board.length * board[0].length;
        Map<List<Integer>,Integer> info = new HashMap<>();
        for(int[] skill: skills){
            if(skill[0] == 1){
                for(int i = skill[1]; i < skill[3] + 1; i++){
                    for(int j = skill[2]; j < skill[4] + 1; j++){
                        info.put(List.of(i,j), info.getOrDefault(List.of(i,j),0) - skill[5]);
                    }
                }
                continue;
            }
            for(int i = skill[1]; i < skill[3] + 1; i++){
                for(int j = skill[2]; j < skill[4] + 1; j++){
                    info.put(List.of(i,j), info.getOrDefault(List.of(i,j),0) + skill[5]);
                }
            }
        }
        for(List<Integer> key : info.keySet()){
            if(board[key.get(0)][key.get(1)] + info.get(key) < 1){
                answer--;
            }
        }
        return answer;
    }
}
