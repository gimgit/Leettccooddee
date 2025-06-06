-- Write your PostgreSQL query statement below
WITH BUYS AS (
    SELECT STOCK_NAME, SUM(PRICE) AS PRICE
    FROM STOCKS
    WHERE OPERATION = 'Buy'
    GROUP BY STOCK_NAME
),
SELLS AS (
    SELECT STOCK_NAME, SUM(PRICE) AS PRICE
    FROM STOCKS
    WHERE OPERATION = 'Sell'
    GROUP BY STOCK_NAME
)
SELECT 
    STOCK_NAME, 
    S.PRICE - B.PRICE AS CAPITAL_GAIN_LOSS
FROM BUYS AS B
INNER JOIN SELLS AS S
USING (STOCK_NAME)
