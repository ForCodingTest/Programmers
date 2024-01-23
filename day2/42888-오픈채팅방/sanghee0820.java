// 16Min

import java.util.*;
class Solution {
    private final String[] type = {"님이 들어왔습니다.", "님이 나갔습니다."};
    private Map<String, String> nameMap = new HashMap<>();
    public List<String> solution(String[] records) {
        
        List<List<String>> answer = new ArrayList<>();
        List<String> result = new ArrayList<>();
        for(String record : records){
            String[] splitedRecord = record.split(" ");
            if(splitedRecord[0].equals("Enter")){
                nameMap.put(splitedRecord[1], splitedRecord[2]);
                answer.add(Arrays.asList(splitedRecord[1], type[0]));
                continue;
            }
            if(splitedRecord[0].equals("Leave")){
                answer.add(Arrays.asList(splitedRecord[1], type[1]));
                continue;
            }
            nameMap.put(splitedRecord[1], splitedRecord[2]);
        }
        for(List<String> data : answer){
            result.add(nameMap.get(data.get(0)) + data.get(1));
        }
        
        return result;
    }
}
