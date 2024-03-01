SELECT distinct(car.CAR_ID), car.CAR_TYPE,
case
    when car.car_type = '세단' then floor(car.daily_fee * 30 * 0.9) 
    when car.car_type = 'SUV' then floor(car.daily_fee * 30 * 0.92)
END AS FEE
FROM CAR_RENTAL_COMPANY_CAR car left outer join CAR_RENTAL_COMPANY_RENTAL_HISTORY his on car.CAR_ID = his.CAR_ID
WHERE (not his.end_date between '2022-11-01'and '2022-11-31') and (not his.start_date between '2022-11-01' and '2022-11-31') and car.car_type in ('세단','SUV')
and ((car.car_type = '세단' and floor(car.daily_fee * 30 * 0.9) between 500000 and 2000000) or (car_type = 'SUV' and floor(car.daily_fee * 30 * 0.92) between 500000 and 2000000))
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC
