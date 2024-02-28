-- concat 구글링. 7:50~7:59

with most_view as (
    select BOARD_ID
    from USED_GOODS_BOARD
    where VIEWS = (select max(VIEWS) from USED_GOODS_BOARD)
)

select concat('/home/grep/src/', b.BOARD_ID, '/', f.FILE_ID, f.FILE_NAME, f.FILE_EXT) as FILE_PATH
from most_view b join USED_GOODS_FILE f using(BOARD_ID)
order by f.FILE_ID desc
