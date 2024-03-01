-- 코드를 입력하세요
SELECT user_id,nickname,concat(CITY," " ,STREET_ADDRESS1," ",STREET_ADDRESS2) "전체주소",
concat(substr(TLNO,1,3),"-",substr(TLNO,4,4),"-",substr(TLNO,8,4)) "전화번호"
from USED_GOODS_BOARD b join USED_GOODS_USER u on b.writer_id=u.user_id
group by user_id
having count(user_id)>=3
order by user_id desc

#7:23