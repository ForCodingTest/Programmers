-- 파이썬과 동일하게 먼저 지정한 반대 순서로 stable sort

select FLAVOR from FIRST_HALF order by TOTAL_ORDER desc, SHIPMENT_ID asc;
