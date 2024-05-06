with candidates as (
    select 
        id,
        lag(id, 1)
            over (
                order by id
            ) as id_lag_one,
        lag(id, 2)
            over (
                order by id
            ) as id_lag_two,
        num,
        lag(num, 1)
            over (
                order by id
            ) as num_day_after,
        lag(num, 2)
            over (
                order by id
            ) as num_two_days_after
    from logs
    )

select distinct num as CONSECUTIVENUMS
from candidates
where 
    num = num_two_days_after
    and num = num_day_after
    and id - 1 = id_lag_one
    and id - 2 = id_lag_two;