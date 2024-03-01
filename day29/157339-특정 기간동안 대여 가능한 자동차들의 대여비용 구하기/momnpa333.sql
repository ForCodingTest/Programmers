-- 코드를 입력하세요
# SELECT *
# from CAR_RENTAL_COMPANY_CAR

# SELECT *
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY

select c.CAR_ID,c.CAR_TYPE,round((1-discount_rate/100)*daily_fee*30,0) FEE
from CAR_RENTAL_COMPANY_CAR c join CAR_RENTAL_COMPANY_DISCOUNT_PLAN t on c.car_type=t.car_type
where car_id not in(
SELECT car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where END_DATE>="2022-11-01") and (c.car_type="세단" or c.car_type="SUV") and duration_type="30일 이상" and round((1-discount_rate/100)*daily_fee*30,0)>=500000 and round((1-discount_rate/100)*daily_fee*30,0)<2000000
order by FEE desc,CAR_TYPE,CAR_ID desc

#7:43
