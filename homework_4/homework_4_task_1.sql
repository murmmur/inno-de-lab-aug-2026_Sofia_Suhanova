--Задание 1
/*
1.Вставить двух новых сотрудников в таблицу Employees (с любыми 
отделами, кроме 'IT').  
2. Выбрать всех сотрудников из таблицы Employees. 
3. Выбрать только FirstName и LastName сотрудников из отдела 'IT'. 
4. Обновить Salary 'Alice Smith' до 65000.00. 
5. Удалить сотрудника 'Eve Davis'. 
6. Проверить все изменения, используя SELECT * FROM Employees;.
*/

--1
insert into Employees (FirstName, LastName, Department, Salary)
values ('Jane', 'Elliot', 'Finance', 65000.00),
('Jack', 'Smith', 'Finance', 63000.00);

--2
select * from Employees;

--3
select FirstName, LastName
from Employees
where Department='IT';

--4
update Employees
set Salary=65000.00
where FirstName='Alice' and LastName='Smith';

--5
delete from Employees
where FirstName='Eve' and LastName='Davis';

--6
select * from Employees;

