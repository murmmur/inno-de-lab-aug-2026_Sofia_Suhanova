--Task 3
/*
 1. Создать нового пользователя PostgreSQL (роль) с именем hr_user и 
паролем. 
2. Предоставить hr_user право SELECT на таблицу Employees. 
3. Тест 1: В новой сессии подключиться как hr_user и попытаться 
выполнить SELECT * FROM Employees;. (Должно сработать). 
Тест 2: Под hr_user попытаться выполнить INSERT нового 
сотрудника (должна возникнуть ошибка доступа).  
4. Как пользователь-администратор, предоставить hr_user права 
INSERT и UPDATE на таблицу Employees. 
5. Тест 3: Как hr_user, попробовать выполнить INSERT и UPDATE 
сотрудника. (Теперь должно сработать). 
*/

--1
create role hr_user with login password 'pass123';

--2
grant select on Employees to hr_user;

--3
grant insert, update on Employees to hr_user;

grant usage, select on all sequences in schema public to hr_user; --доступ к последовательности
