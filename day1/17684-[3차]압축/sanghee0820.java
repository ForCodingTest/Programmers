// 22 Min
import java.util.*;
class Solution {
    private Map<String, Integer> dictionary = new HashMap<>();
    
    public void initDictionary(){
        for(int i = 0; i < 26; i++){
            dictionary.put(String.valueOf((char)('A' + i)), i + 1);
        }
    }
    
    public List<Integer> solution(String msg) {
        List<Integer> result = new ArrayList<>();
        initDictionary();
        int dicSize = 26;
        for(int i = 0; i < msg.length();){
            String current = String.valueOf(msg.charAt(i));
            while(dictionary.containsKey(current) && ++i < msg.length()){
                current += String.valueOf(msg.charAt(i));
            }
            
            if(!dictionary.containsKey(current)){
                dictionary.put(current, ++dicSize); 
                result.add(dictionary.get(current.substring(0, current.length()-1)));
                continue;
            }
            
                result.add(dictionary.get(current));
        }
        return result;
    }
}
