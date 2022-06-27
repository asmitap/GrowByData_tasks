--1.Create table Employee and Department with Department Id of Employee foreign key to table Department.

-- create database
create database company_details;

-- create table department
create table department(
id serial primary key not null,
name varchar(100)
);

--create employee table
create table employee(
id serial primary key not null,
name varchar(100),
department_id int,
salary varchar(100),
active int,
foreign key(department_id) references department(id)
);

--insert into table department 
insert into department(name) 
values ('IT'), ('Admin'), ('HR'), ('Accounts'), ('Health');

--insert into table employee 
insert into employee(name, department_id, salary, active) 
values ('John',1,2000,1),('Sean',1,4000, 1),('Eric',2,2000, 1),('Nancy',2,2000, 1),('Lee',3,'3000',1),
('Steven',4,2000, 1),('Matt',1,5000, 1),('Sarah',1,2000,0);

-- 2.	Write a query to get employee list in ascending order of their salary.
select * from employee order by salary ASC;

-- 3.	Write a query to get distinct salary from Employee table.
select distinct salary from employee;

-- 4.	Write a query to find total number of active employees.
SELECT COUNT(active) FROM employee where (active=1);

--5.	Update the Department of Nancy to HR.
update department set name = 'HR' from employee  where department.id = 2;

--6.	Write a query to get a record of employee with highest and second highest salary.
select * FROM employee ORDER BY salary desc limit 2;

--7.	Write a query to get department name of each employee.
select employee.name, department.name from employee join department on employee.department_id =department.id;

--8.	Write a query to get department name with maximum employee count.
select department.name, count(employee.department_id) as emp_count
from employee join department on employee.department_id = department.id
group by (department.name, employee.department_id)
order by emp_count desc limit 1; 

--9.	Write a query to get departments where no Employee is assigned.
select name from department where department.id not in (select department_id from employee);

--10.	Write a query to get list of employee and salary with same salary.
select name, salary from employee where salary=(select salary from employee group by salary having count(salary)>1);


