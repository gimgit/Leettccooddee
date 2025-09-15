-- # Write your MySQL query statement below

WITH UNBANNED AS (
    SELECT users_id FROM USERS
    WHERE BANNED = 'No'
),
BEFORE_ROUND AS (
SELECT 
  convert(request_at  , date) as Day,
  SUM(CASE WHEN status != 'completed' THEN 1 ELSE 0 END) /
  count(*) AS RATE
FROM TRIPS AS T
JOIN UNBANNED AS C
ON T.CLIENT_ID = C.USERS_ID
JOIN UNBANNED AS D
ON T.DRIVER_ID = D.USERS_ID
WHERE request_at between '2013-10-01' and '2013-10-03'
group by convert(request_at  , date)
)
SELECT Day, ROUND(RATE, 2) AS "Cancellation Rate" FROM BEFORE_ROUND;
