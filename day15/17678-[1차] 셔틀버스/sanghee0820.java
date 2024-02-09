import java.util.*;
class Solution {
    public String solution(int n, int t, int m, String[] timetable) {
        String answer = "";
        Arrays.sort(timetable, (a,b) ->{
            String[] aSplit = a.split(":");
            String[] bSplit = b.split(":");
            return (Integer.valueOf(aSplit[0]) * 60 + Integer.valueOf(aSplit[1]))
                - (Integer.valueOf(bSplit[0]) * 60 + Integer.valueOf(bSplit[1]));
        });
        Stack<String> timeStack = new Stack<>();
        timeStack.addAll(Arrays.asList(timetable));
        Queue<String> timeQueue = new LinkedList<>(timeStack);
        String maxTime = "";
        for(int i = 0; i < n; i++){
            int time = 540 + t * i;
            int cnt = 0;
            Stack<String> temp = new Stack();
            while(!timeQueue.isEmpty() && cnt < m){
                String current = timeQueue.peek();
                String[] currentSplit = current.split(":");
                if(Integer.valueOf(currentSplit[0]) * 60 + Integer.valueOf(currentSplit[1])
                  <= time){
                    temp.add(timeQueue.remove());
                    cnt++;
                    continue; 
                }  
                break;
            }
            if(temp.size() == m){
                String[] lastTime = temp.pop().split(":");
                int tempTime = Integer.valueOf(lastTime[0])*60 + Integer.valueOf(lastTime[1]) - 1;
                maxTime = String.format("%02d:%02d", (int)Math.floor((double)tempTime/60), tempTime%60);
                continue;
            }else{
                
                maxTime = String.format("%02d:%02d", (int)Math.floor((double)time/60), time%60);
            }
        }
        
        // System.out.println(maxTime);
        return maxTime;
    }
}
