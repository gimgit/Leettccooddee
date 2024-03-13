SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE SALARY <> (
    SELECT MAX(Salary) FROM Employee
)