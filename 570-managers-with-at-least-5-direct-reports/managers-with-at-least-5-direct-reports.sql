# Write your MySQL query statement below
SELECT e.name
FROM Employee e
JOIN Employee a
ON e.id=a.managerId
GROUP BY e.id,e.name
HAVING COUNT(e.id)>=5;