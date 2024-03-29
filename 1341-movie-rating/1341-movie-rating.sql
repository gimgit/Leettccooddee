# Write your MySQL query statement below
WITH USER AS (
    SELECT U.NAME AS RESULTS
    FROM USERS AS U
    INNER JOIN MOVIERATING AS MR
    ON U.USER_ID = MR.USER_ID
    GROUP BY U.USER_ID
    ORDER BY 
        COUNT(*) DESC,
        U.NAME ASC
    LIMIT 1
),

MOVIE AS (
    SELECT 
        M.TITLE
    FROM MOVIERATING AS MR
    INNER JOIN MOVIES AS M
    ON MR.MOVIE_ID = M.MOVIE_ID
    WHERE DATE_FORMAT(CREATED_AT , '%y-%m') = '20-02'
    GROUP BY MR.MOVIE_ID
    ORDER BY
        AVG(MR.RATING) DESC,
        M.TITLE ASC
    LIMIT 1
)

SELECT * FROM USER
UNION ALL
SELECT * FROM MOVIE