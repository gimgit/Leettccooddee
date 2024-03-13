with shift as(
    select
        case
            WHEN ID % 2 AND ID = (SELECT COUNT(*) FROM SEAT)
                THEN ID
            WHEN ID % 2
                THEN ID + 1
            ELSE ID - 1
        END AS NEW_ID,
        STUDENT
    FROM SEAT
)


select 
    NEW_ID AS ID,
    STUDENT
FROM SHIFT
ORDER BY ID;
