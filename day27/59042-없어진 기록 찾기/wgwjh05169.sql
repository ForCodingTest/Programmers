-- 7:55~8:05

select o.ANIMAL_ID, o.NAME
from ANIMAL_OUTS o
where o.ANIMAL_ID not in (select i.ANIMAL_ID from ANIMAL_INS i)
order by o.ANIMAL_ID
