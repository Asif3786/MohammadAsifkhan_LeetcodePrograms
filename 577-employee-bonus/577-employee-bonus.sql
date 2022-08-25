/* Write your T-SQL query statement below */
select a.name,b.bonus from Employee a left join 
bonus b on a.empId=b.empId 
where b.bonus is null or b.bonus<1000



