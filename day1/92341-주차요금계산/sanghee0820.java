// 30Min
import java.util.*;
class Solution {
    private Map<Integer, List<List<String>>> carRecords = new HashMap();
    
    public int getFee(int[] fees, List<List<String>> record){
        int fee = 0;
        int totalTime = 0;
        for(int i = 0; i < record.size(); ){
            List<String> input = record.get(i++);
            List<String> output = Arrays.asList("23:59", "OUT");
            if(i < record.size()){
                output = record.get(i++);
            }
            String[] parsedInputTime = input.get(0).split(":"); 
            String[] parsedOutputTime = output.get(0).split(":"); 
            int inputTime = Integer.valueOf(parsedInputTime[0]) * 60 + Integer.valueOf(parsedInputTime[1]);
            int outputTime = Integer.valueOf(parsedOutputTime[0]) * 60 + Integer.valueOf(parsedOutputTime[1]);
            int time = outputTime - inputTime;
            totalTime += time;
        }
        
        System.out.println(totalTime);
        
        fee += fees[1];
        totalTime -= fees[0];
        if(totalTime > 0){
            fee += Math.ceil((double)totalTime / fees[2]) * fees[3];
        }
        return fee;
    }
    public int[] solution(int[] fees, String[] records) {
        for(String record : records){
            String[] parsedRecord = record.split(" ");
            if(!carRecords.containsKey(Integer.valueOf(parsedRecord[1]))){
                carRecords.put(Integer.valueOf(parsedRecord[1]), new ArrayList<>(new ArrayList<>()));
            }
            carRecords.get(Integer.valueOf(parsedRecord[1])).add(
                                                Arrays.asList(parsedRecord[0], parsedRecord[2])
                                               );
        }
        List<Integer> keySet = new ArrayList<>(carRecords.keySet());
        Collections.sort(keySet);
        
        int[] result = new int[keySet.size()];
        for(int i = 0; i < keySet.size(); i++){
            result[i] = getFee(fees, carRecords.get(keySet.get(i)));
        }
        return result;
    }
}
