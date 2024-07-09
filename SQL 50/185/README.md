# The solution is available below and you can view my breakdown using the link below


WITH RankedSalaries AS (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) AS SalaryRank
    FROM
        Employee e
        INNER JOIN Department d ON e.departmentId = d.id
)
SELECT
    Department, Employee, Salary
FROM
    RankedSalaries
WHERE
    SalaryRank <= 3; 

