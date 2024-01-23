// 18 Min

import java.util.*;
class Solution {
    private final String[][] categories = {{"R","T"}, {"C", "F"}, {"J", "M"}, {"A", "N"}};
    private Map<String, Integer> getScores = new HashMap<>();
    private int[] score = {0, 1, 2, 3};
    public void scoreInit(){
        for(String[] category : categories){
            for(String data : category){
                getScores.put(data, 0);
            }
        }
    }
    public String solution(String[] surveys, int[] choices) {
        String answer = "";
        scoreInit();
        for(int i = 0; i < surveys.length; i++){
            String survey = surveys[i];
            int choice = choices[i];
            //0일때 주의
            if(choice - 4 > 0){
                String key = String.valueOf(survey.charAt(1));
                getScores.put(key, getScores.get(key) + score[choice - 4]);
                continue;
            }
            String key = String.valueOf(survey.charAt(0));
            getScores.put(key, getScores.get(key) + score[4 - choice]);
        }
        
        for(int i = 0; i < 4; i++){
            String keyA = categories[i][0];
            String keyB = categories[i][1];
            int valueA = getScores.get(keyA);
            int valueB = getScores.get(keyB);
            if(valueA > valueB){
                answer += keyA;
                continue;
            }
            if( valueA < valueB){
                answer += keyB;
                continue;
            }
            answer += keyA;
        }
        
        return answer;
    }
}
