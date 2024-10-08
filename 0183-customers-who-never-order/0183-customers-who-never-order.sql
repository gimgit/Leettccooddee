WITH ORDERED AS (
    SELECT DISTINCT CUSTOMERID FROM ORDERS
)
SELECT NAME AS CUSTOMERS
FROM CUSTOMERS AS C
LEFT JOIN ORDERS AS O
ON C.ID = O.CUSTOMERID
WHERE O.CUSTOMERID IS NULL;