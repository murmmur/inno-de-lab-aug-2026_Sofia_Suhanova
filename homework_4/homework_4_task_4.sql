--Задание 4
/*
1. Увеличить Salary всех сотрудников в отделе 'HR' на 10%. 
2. Обновить Department любого сотрудника с Salary выше 70000.00 
на 'Senior IT'. 
3. Удалить всех сотрудников, которые не назначены ни на один проект в 
таблице EmployeeProjects. Подсказка: Используйте подзапрос NOT 
EXISTS или LEFT JOIN 
4. В рамках одной транзакции, вставить новый проект и назначить на 
него двух существующих сотрудников с определенным количеством 
HoursWorked в EmployeeProjects. 
*/

--1
update Employees 
set salary=salary*1.1
where Department='HR';

select * from Employees;

--2
update Employees 
set Department='Senior IT'
where Salary >=70000.00;

select * from Employees;

--3
delete from Employees 
where not exists (
select 1
from EmployeeProjects 
where EmployeeProjects.EmployeeID = Employees.EmployeeID 
);

select * from Employees;

--4
begin;

insert into Projects (ProjectName, Budget, StartDate,EndDate)
values ('Project Promotion',150000.00,'2026-03-15','2026-12-15');

insert into EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
values (1,4,80), 
(3,4,100);

commit;

select * from Projects;
select * from EmployeeProjects;