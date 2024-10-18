-- Write your PostgreSQL query statement below
SELECT
    DISTINCT
        T.ID,
        CASE
            WHEN T.P_ID IS NULL THEN 'Root'
            WHEN T_JOINED.ID IS NULL THEN 'Leaf'
            ELSE 'Inner'
        END AS "TYPE"
FROM TREE AS T
LEFT JOIN TREE AS T_JOINED
ON T.ID = T_JOINED.P_ID