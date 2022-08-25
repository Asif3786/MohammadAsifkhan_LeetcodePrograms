/* Write your T-SQL query statement below */
select emp.name as Employee from Employee as emp join Employee as Man
on emp.salary>Man.salary and emp.managerid=Man.id
