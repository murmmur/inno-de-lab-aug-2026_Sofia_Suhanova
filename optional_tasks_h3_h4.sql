--Optional tasks

--h3 optional task
select c.first_name||' '||c.last_name as full_name, 
c.country,
count (o.order_id) as total_orders,
sum(o.amount) as total_amount
from customers c 
join orders o on c.customer_id=o.customer_id
where exists (
select 1
from shippings s
where s.customer=c.customer_id 
and s.status='Delivered'
)
group by c.customer_id, c.first_name, c.last_name, c.country
having count(o.order_id)>=2

--h4 optional task
--1
select p.ProjectName
from projects p
join EmployeeProjects ep on p.projectid =ep.projectid 
join employees e on ep.employeeid=e.employeeid 
where e.firstname ='Bob' and e.lastname = 'Johnson'
and ep.hoursworked >150;

--2
update projects p
set budget=budget*1.1
from employeeprojects ep
join employees e on ep.employeeid = e.employeeid 
where p.projectid = ep.projectid 
and e.department='IT';

select * from projects;

--3
update projects 
set enddate=startdate + interval '1 year'
where enddate is null;

select * from projects;

--4
begin;

with 
new_employee as (
insert into employees (FirstName, LastName, Department, Salary)
values ('Kae','Doughh', 'IT', 63000.00)
returning employeeid
),
project_id as (
select projectid from projects where projectname='Website Redesign'
)
insert into employeeprojects (employeeid,projectid,hoursworked)
select new_employee.employeeid, project_id.projectid, 80
from new_employee, project_id;

commit;

select * from employees;
select * from employeeprojects;
