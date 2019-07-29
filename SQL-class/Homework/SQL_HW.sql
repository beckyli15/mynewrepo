select * from departments limit 100
select * from dept_emp limit 100
select * from dept_manager limit 100
select * from employees limit 100
select * from salaries limit 100
select * from titles limit 100
drop table departments
create table departments(dept_no VARCHAR primary key, dept_name VARCHAR);
DROP TABLE dept_emp
create table dept_emp(emp_no INT, dept_no VARCHAR, foreign key (dept_no) references departments(dept_no), from_date VARCHAR, to_date VARCHAR, foreign key (emp_no) references employees(emp_no));
drop table dept_manager
create table dept_manager(dept_no VARCHAR, FOREIGN KEY(dept_no) references departments(dept_no), emp_no INT, FOREIGN KEY(emp_no) references employees(emp_no), from_date VARCHAR, to_date VARCHAR );
create table employees(emp_no int PRIMARY KEY, birth_date VARCHAR, first_name VARCHAR, last_name VARCHAR, gender VARCHAR, hire_date VARCHAR);
drop table salaries
create table salaries(emp_no int, FOREIGN KEY(emp_no) references employees(emp_no), salary int, from_date VARCHAR, to_date VARCHAR );
drop table titles
create table titles(emp_no int, FOREIGN KEY(emp_no) references employees(emp_no), title VARCHAR, from_date VARCHAR, to_date VARCHAR);

