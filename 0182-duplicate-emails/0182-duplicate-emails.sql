# Write your MySQL query statement below
Select Email 
FROM Person
GROUP BY Email
HAVING COUNT(*)>1;
