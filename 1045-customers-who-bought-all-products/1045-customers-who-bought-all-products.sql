# Write your MySQL query statement below
SELECT 
    CUSTOMER_ID
FROM CUSTOMER
GROUP BY CUSTOMER_ID
HAVING COUNT(DISTINCT PRODUCT_KEY) = (
    SELECT COUNT(DISTINCT PRODUCT_KEY) FROM PRODUCT
);
