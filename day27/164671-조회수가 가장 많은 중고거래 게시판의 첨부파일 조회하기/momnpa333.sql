-- 코드를 입력하세요
SELECT concat('/home/grep/src/',b.board_id,"/",f.file_id,f.file_name,f.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD b join USED_GOODS_FILE f on b.BOARD_ID=f.BOARD_ID
where b.BOARD_ID=(
select BOARD_ID
from USED_GOODS_BOARD
order by views desc
limit 1
)
order by f.file_id desc
