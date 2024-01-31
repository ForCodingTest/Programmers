import java.util.*;

class Solution {
    
    Set<String> result = new HashSet<>();
    
    public void makeResult(List<List<String>> banned, int count, List<String> combine){
        if(count == banned.size()){
            List<String> temp = new ArrayList<>(combine);
            Collections.sort(temp);
            String str = "";
            for(String data : temp){
                str += data;
            }
            result.add(str);
            return;
        }
        for (String element : banned.get(count)) {
            if(combine.contains(element)){
                continue;
            }
            combine.add(element);
            makeResult(banned, count + 1, combine);
            combine.remove(combine.size() - 1);
        }
    }
    public int solution(String[] user_id, String[] banned_id) {
        int answer = 0;
        List<List<String>> parsedBannedId = new ArrayList<>();
        List<List<String>> banned = new ArrayList<>();
        
        for(int i = 0; i < banned_id.length; i++){
            String[] parsedId = banned_id[i].split("(?=\\*)|(?<=\\*)");
            List<String> ban = new ArrayList<>();
            for(String id : user_id){
                if(id.length() != banned_id[i].length()){
                    continue;
                }
                String remain = id;
                for(String parsed : parsedId){
                    String tempRemain = remain.substring(0, parsed.length());
                    if(parsed.equals("*")){
                        remain = remain.substring(parsed.length());
                        continue;
                    }
                    if(!tempRemain.equals(parsed)){
                        break;
                    }
                    remain = remain.substring(parsed.length());
                }
                if(remain.equals("")){
                    ban.add(id);
                }
            }
            banned.add(ban);
        }
        makeResult(banned, 0, new ArrayList<>());
        return result.size();
    }
}
