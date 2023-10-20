# Write your MySQL query statement below

Select Department.name as Department,Employee.name as Employee, Employee.salary as Salary from Employee Inner Join Department on employee.departmentId = department.id Where(Employee.departmentId,Employee.salary) In(Select DepartmentId,Max(salary)
From Employee
Group by departmentId
);
