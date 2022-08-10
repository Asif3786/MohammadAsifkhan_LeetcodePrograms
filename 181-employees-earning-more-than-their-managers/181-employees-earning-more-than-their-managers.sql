select emp.name as Employee from Employee emp
where emp.salary > (select salary from Employee where emp.managerid=id)
