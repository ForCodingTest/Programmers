// 30 Min & 구글링
class Solution {
    public String solution(String new_id) {
        String answer = "";
        String new_id_1 = new_id.toLowerCase();
        String new_id_2 = new_id_1.replaceAll("[^a-z0-9\\-\\_\\.]", "");
        String new_id_3 = new_id_2.replaceAll("\\.{2,}", ".");
        String new_id_4 = new_id_3.replaceAll("^\\.|\\.$", "");
        if (new_id_4.isEmpty()) {
            new_id_4 = "a";
        }
        if (new_id_4.length() >= 16) {
            new_id_4 = new_id_4.substring(0, 15);
            new_id_4 = new_id_4.replaceAll("\\.$", "");
        }
        
        while (new_id_4.length() <= 2) {
            new_id_4 += new_id_4.charAt(new_id_4.length() - 1);
        }
        return new_id_4;
    }
}
