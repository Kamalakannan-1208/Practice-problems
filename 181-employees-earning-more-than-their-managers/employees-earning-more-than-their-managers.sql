-- Write your PostgreSQL query statement below
select m.name as employee
from employee e
join employee m on e.id = m.managerid
where e.salary < m.salary;