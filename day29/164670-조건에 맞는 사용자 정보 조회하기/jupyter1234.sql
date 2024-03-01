SELECT USER_ID, NICKNAME, CONCAT(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) AS 전체주소, CONCAT(SUBSTRING(TLNO,1,3),'-',SUBSTRING(TLNO,4,4),'-',SUBSTRING(TLNO,8,4)) AS 전화번호
FROM (select writer_id, count(*) from used_goods_board group by writer_id having count(*) >= 3) board inner join USED_GOODS_USER on USED_GOODS_USER.user_id = board.writer_id
order by USER_ID desc
