//28Mins

import java.util.*;
import java.time.*;
import java.time.format.*;
class Solution {
    private Map<String, Integer> termMap = new HashMap<>();
    public List<Integer> solution(String today, String[] terms, String[] privacies) {
        List<Integer> result = new ArrayList<>();
        for(String term : terms){
            String[] splitedTerm = term.split(" ");
            termMap.put(splitedTerm[0], Integer.valueOf(splitedTerm[1]));
        }
        for(int i = 0; i < privacies.length; i++){
            if(isDeleted(privacies[i], today)){
                result.add(i + 1);
            }
        }
        return result;
    }
    
    public boolean isDeleted(String privacy, String today){
        
        String[] splitedPrivacy = privacy.split(" ");
        String[] splitedDate = splitedPrivacy[0].split("\\.");
        int[] date = new int[3];
        for(int i = 0; i < 3; i++){
            date[i] = Integer.valueOf(splitedDate[i]);
        }
        
        date[1] += termMap.get(splitedPrivacy[1]);
        date[2]--;
        
        if(date[2] == 0){
            date[1]--;
            date[2] = 28;
        }
        while(date[1] > 12){
            date[0]++;
            date[1] -= 12;
        }
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy.MM.dd");
        LocalDate endDate = LocalDate.of(date[0], date[1], date[2]);
        LocalDate nowDate = LocalDate.parse(today, formatter);
        
        return nowDate.isAfter(endDate);
    }
}
