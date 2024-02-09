import java.util.*;
class Solution {
    private Map<String, Integer> orderMap = new HashMap<>();
    private List<String> selectedMenu = new ArrayList<>();
    private List<String> result = new ArrayList<>();
    public List<String> solution(String[] orders, int[] course) {
        initMap(orders);
        for(int cnt : course){
            Map<String, Integer> courseCount = new HashMap<>();
            DFS(0, 0, new String[cnt], orders, courseCount);
            List<Integer> values = new ArrayList<>(courseCount.values());
            Collections.sort(values);
            for(String key : courseCount.keySet()){
                if(courseCount.get(key) == values.get(values.size() - 1)){
                    result.add(key);
                }
            }
        }
        Collections.sort(result);
        return result;
    }
    
    public void DFS(int curSize, int start, String[] selects,
                    String[] orders, Map<String, Integer> courseCount){
        if(curSize == selects.length){
            int cnt = 0;
            for(String order : orders){
                boolean flag = true;
                for(String select : selects){
                    if(!order.contains(select)){
                        flag = false;
                        break;
                    }
                }
                if(flag){ 
                    cnt ++;
                }
            }
            if(cnt > 1){
                courseCount.put(String.join("", selects), cnt);
            }
            return;
        }
        for(int i = start; i < selectedMenu.size(); i++){
            selects[curSize] = selectedMenu.get(i);
            DFS(curSize + 1, i + 1, selects,  orders, courseCount);
        }
    }
    
    public void initMap(String[] orders){
        for(String order : orders){
            String[] foods = order.split("");
            for(String food : foods){ 
                if(!orderMap.containsKey(food)){
                    orderMap.put(food, 0);
                }
                orderMap.put(food, orderMap.get(food) + 1);
            }
        }
        for(String key : orderMap.keySet()){
            if(orderMap.get(key) > 1){
                selectedMenu.add(key);
            }
        }
    }
}
