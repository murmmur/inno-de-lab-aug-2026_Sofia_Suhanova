--Task 2
/*
1. Создать новую таблицу с именем Departments со столбцами: 
DepartmentID (SERIAL PRIMARY KEY), DepartmentName 
(VARCHAR(50), UNIQUE, NOT NULL), Location (VARCHAR(50)). 
2. Изменить таблицу Employees, добавив новый столбец с именем 
Email (VARCHAR(100)). 
3. Заполнить столбец Email для всех текущих сотрудников 
уникальными значениями (например, через UPDATE). 
4. Добавить ограничение UNIQUE к столбцу Email в таблице 
Employees. 
5. Переименовать столбец Location в таблице Departments в 
OfficeLocation. 
*/

--1
create table Departments(
DepartmentID SERIAL primary key,
DepartmentName VARCHAR(50) unique not null,
Location varchar(50)
);

--2
alter table Employees add column Email varchar(100);

--3
update Employees
set Email=LastName||'.'||FirstName||'.'||'company@gmail.com';

--4
alter table Employees add constraint UK_Employees_Email unique(Email);

--5
alter table Departments rename column Location to OfficeLocation;

--check
select * from Employees;
select * from Departments;