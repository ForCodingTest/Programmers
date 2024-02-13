import java.util.*;

class Solution {
    Stack<Integer> deleted = new Stack<>();
    int[] deletedAry;
    public String solution(int n, int cur, String[] cmd) {
        StringBuilder answer = new StringBuilder();
        deletedAry = new int[n];
        answer.append("O".repeat(n));
        int maxIndex = n - 1;
        for(String command : cmd){
            String[] info = command.split(" ");
            if(info[0].equals("D")){
                cur = down(cur, Integer.parseInt(info[1]), n);
                continue;
            } 
            if(info[0].equals("U")){
                cur = up(cur, Integer.parseInt(info[1])); 
                continue;
            }
            if(info[0].equals("C")){
                deleted.add(cur);
                deletedAry[cur] = 1;
                if(cur == maxIndex){
                    cur = up(cur, 1);
                    maxIndex = cur;
                }else{
                    cur = down(cur, 1, n);
                }
                continue;
            }
            deletedAry[deleted.pop()] = 0;
        }
        while(!deleted.isEmpty()){
            answer.setCharAt(deleted.pop(), 'X');
        }
        return answer.toString();
    }
    
    public int up(int cur, int x){
        while(x > 0 && cur > -1){
            cur--;
            if(deletedAry[cur] == 1){
                continue;
            }
            x--;
        }
        return cur;
    }
    
    public int down(int cur, int x, int n){
        while(cur < n - 1 && x > 0){
            cur++;
            if(deletedAry[cur] == 1){
                continue;
            }
            x--;
        }
        
        return cur;
    }
}
