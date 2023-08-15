-- show global variables like 'local_infile';
-- set global local_infile=true;
-- SELECT * FROM teachers_salaries;
-- DROP DATABASE IF EXISTS teachers_salaries;
-- CREATE TABLE employees(
--   ID INT PRIMARY KEY NOT NULL,
--   name VARCHAR(255),
--   email VARCHAR(255)
-- )
SELECT * FROM employees;
ALTER TABLE employees
MODIFY COLUMN ID INT NOT NULL AUTO_INCREMENT,
DROP PRIMARY KEY,
ADD PRIMARY KEY(ID);


SELECT column1, column2, ...
FROM table_name
WHERE condition;
WHERE column LIKE '%a'

