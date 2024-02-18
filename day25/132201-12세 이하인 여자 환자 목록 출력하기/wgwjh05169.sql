-- ifnull(column, value)
-- case when {condition} then {value} when ... else {value} end
-- null 검사는 is null, is not null

# select pt_name, pt_no, gend_cd, age, ifnull(tlno, 'NONE') as tlno
#     from patient
#     where age <= 12 and gend_cd = 'W'
#     order by age desc, pt_name asc;
    
select pt_name, pt_no, gend_cd, age,
    (case
        when tlno is NULL then "NONE"
        else tlno
    end) as tlno
    from patient
    where age <= 12 and gend_cd = 'W'
    order by age desc, pt_name asc;
