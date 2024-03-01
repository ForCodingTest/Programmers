-- 7:40~7:46

with writer as (
    select WRITER_ID
    from USED_GOODS_BOARD
    group by WRITER_ID
    having count(*) >= 3
)

select u.USER_ID, u.NICKNAME, (
        concat(u.CITY, ' ', u.STREET_ADDRESS1, ' ', u.STREET_ADDRESS2)
    ) as '전체주소', (
        concat(
            substring(u.tlno, 1, 3), '-',
            substring(u.tlno, 4, 4), '-',
            substring(u.tlno, 8, 4)
        )
    ) as '전화번호'
from writer w join USED_GOODS_USER u on w.WRITER_ID = u.USER_ID
order by u.USER_ID desc

-- 게시물을 3건 이상 등록한 사용자
-- 사용자 ID, 닉네임, 전체주소, 전화번호
