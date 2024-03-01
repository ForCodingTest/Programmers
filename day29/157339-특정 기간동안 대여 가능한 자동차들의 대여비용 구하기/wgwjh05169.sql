-- ~7:40

with cars as (
    select CAR_ID, CAR_TYPE, DAILY_FEE
    from CAR_RENTAL_COMPANY_CAR
    where CAR_TYPE in ('세단', 'SUV')
), rentable as (
    select distinct c.CAR_ID, c.CAR_TYPE, c.DAILY_FEE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY h join cars c using(CAR_ID)
    where c.CAR_ID not in (
        select CAR_ID
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where ('2022-11-01' < END_DATE) or (START_DATE > '2022-11-30')
    )
), rent_fee as (
    select c.CAR_ID, c.CAR_TYPE, round(c.DAILY_FEE * (100 - p.DISCOUNT_RATE) / 100 * 30) as FEE
    from rentable c join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
        on (c.CAR_TYPE = p.CAR_TYPE and p.DURATION_TYPE = '30일 이상')
)

select * from rent_fee
where FEE >= 500000 and FEE <= 2000000
order by FEE desc, CAR_TYPE, CAR_ID desc


-- 세단 혹은 SUV
-- 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능
-- 30일간의 대여 금액이 50만원 이상 200만원 미만
-- 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE)
-- 대여 금액을 기준으로 내림차순, 자동차 종류를 기준으로 오름차순, 자동차 ID를 기준으로 내림차순 
