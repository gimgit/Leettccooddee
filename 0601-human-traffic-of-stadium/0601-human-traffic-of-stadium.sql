SELECT ID, 
    visit_date,
    people
FROM (
    SELECT 
        ID,
        PEOPLE,
        VISIT_DATE,
        LEAD(people, 1) OVER (ORDER BY id) nxt, 
        LEAD(people, 2) OVER (ORDER BY id) nxt2,
        LAG(people, 1) OVER (ORDER BY id) pre,
        LAG(people, 2) OVER (ORDER BY id) pre2
    FROM Stadium
) base_table 
WHERE (
    base_table.people >= 100 
    AND base_table.nxt >= 100 AND (
    base_table.nxt2 >= 100) 
    OR (base_table.people >= 100 AND base_table.nxt >= 100
    )    
AND (
    base_table.pre >= 100)  
    OR (base_table.people >= 100 AND base_table.pre >= 100 
)
AND base_table.pre2 >= 100) 