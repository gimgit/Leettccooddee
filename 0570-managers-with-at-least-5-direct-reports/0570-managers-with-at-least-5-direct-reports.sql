-- Write your PostgreSQL query statement below
WITH MATERIAL AS (
    SELECT
        managerId
    FROM EMPLOYEE
    GROUP BY managerId
    HAVING COUNT(DISTINCT ID) > 4
)

SELECT NAME FROM EMPLOYEE WHERE ID IN (
    SELECT managerID AS MANAGER_ID FROM MATERIAL
)