// 20mins
import java.util.*;

// 선물지수 : 이번달까지 자신이 친구들에게 준 선물의수 - 받은선물
// 주고받은 기록 있음 -> 더많이 준사람 선물하나
// 없거나 같음 -> 선물지수더 높은사람이 받음 -> 선물지수도 같으면 없음.


class Solution {
    private int[][] giftTable;
    private Map<String, Integer> nameMap = new HashMap<>();
    private Map<String, Integer> getGift = new HashMap<>();
    
    public void initGiftTable(String[] gifts){
        for(String gift : gifts){
            String[] giftInfo = gift.split(" ");
            giftTable[nameMap.get(giftInfo[0])][nameMap.get(giftInfo[1])]++;
        }
    }
    public void initNameMap(String[] friends){
        giftTable = new int[friends.length][friends.length];
        int i = 0;
        for(String friend : friends){
            nameMap.put(friend, i++);
            getGift.put(friend, 0);
        }
    }

    public int solution(String[] friends, String[] gifts) {
        
        int answer = 0;
        initNameMap(friends);
        initGiftTable(gifts);
        for(String key : nameMap.keySet()){
            int index = nameMap.get(key);
            for(int i = 0; i < nameMap.keySet().size(); i++){
                if(i == index){
                    continue;
                }
                if(giftTable[index][i]/*준것*/ > giftTable[i][index]/*받은것*/){
                    getGift.put(key, getGift.get(key) + 1);
                    continue;
                }
                if(giftTable[index][i]/*준것*/ == giftTable[i][index]/*받은것*/){
                    int giftRatio1 = 0; // key의 giftRatio
                    int giftRatio2 = 0; // 비교 대상의 giftRatio
                    for(int j = 0; j < nameMap.keySet().size(); j++){
                        giftRatio1 += giftTable[index][j];
                        giftRatio2 += giftTable[i][j];
                        giftRatio1 -= giftTable[j][index];
                        giftRatio2 -= giftTable[j][i];
                    }
                    if(giftRatio1 > giftRatio2){
                        getGift.put(key, getGift.get(key) + 1);
                        continue;                    
                    }
                    
                }
            }
        }
        for(int values : getGift.values()){
            if(answer < values){
                answer = values;
            }
        }
        return answer;
    }
}
