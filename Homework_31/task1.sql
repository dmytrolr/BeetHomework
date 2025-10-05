-- 1. Ім’я, прізвище, номер відділу та назва відділу
SELECT e.first_name, e.last_name, e.department_id, d.depart_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- 2. Ім’я, прізвище, назва відділу, місто та область
SELECT e.first_name, e.last_name, d.depart_name, l.city, l.state_province
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id;

-- 3. Ім’я, прізвище, номер і назва відділу для співробітників з відділів 80 або 40
SELECT e.first_name, e.last_name, e.department_id, d.depart_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.department_id IN (80, 40);

-- 4. Всі відділи, включаючи ті, де немає співробітників
SELECT d.depart_name, e.employee_id
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id;

-- 5. Ім’я співробітника + ім’я його керівника
SELECT e.first_name || ' ' || e.last_name AS employee_name,
       m.first_name || ' ' || m.last_name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;

-- 6. Посада, повне ім’я, різниця між максимальною зарплатою та зарплатою співробітника
SELECT j.job_title,
       e.first_name || ' ' || e.last_name AS employee_name,
       j.max_salary - e.salary AS salary_gap
FROM employees e
JOIN jobs j ON e.job_id = j.job_id;

-- 7. Посада та середня зарплата співробітників
SELECT j.job_title, AVG
