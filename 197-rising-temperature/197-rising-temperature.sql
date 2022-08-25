/* Write your T-SQL query statement below */
select a.id from weather a join weather b 
on a.temperature>b.temperature 
and datediff(day,b.recordDate,a.recordDate)=1