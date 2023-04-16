-- создаем базу данных
CREATE DATABASE practice_three;

-- подключаемся к базе данных
USE practice_three;

-- создаем таблицу
CREATE TABLE `staff`
(
`id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
`firstname` VARCHAR(20) NOT NULL,
`lastname` VARCHAR(20) NOT NULL,
`post` VARCHAR(10) NOT NULL,
`seniority` INT UNSIGNED NULL,
`salary` DECIMAL(10,2) NOT NULL,
`age` INT UNSIGNED NOT NULL
);

INSERT INTO `staff` (`firstname`, `lastname`, `post`, `seniority`, `salary`, `age`)
VALUES
('Вася', 'Петров', 'Начальник', '40', 100000, 60),
('Петр', 'Власов', 'Начальник', '8', 70000, 30),
('Катя', 'Катина', 'Инженер', '2', 70000, 25),
('Саша', 'Сасин', 'Инженер', '12', 50000, 35),
('Иван', 'Иванов', 'Рабочий', '40', 30000, 59),
('Петр', 'Петров', 'Рабочий', '20', 25000, 40),
('Сидр', 'Сидоров', 'Рабочий', '10', 20000, 35),
('Антон', 'Антонов', 'Рабочий', '8', 19000, 28),
('Юрий', 'Юрков', 'Рабочий', '5', 15000, 25),
('Максим', 'Максимов', 'Рабочий', '2', 11000, 22),
('Юрий', 'Галкин', 'Рабочий', '3', 12000, 24),
('Людмила', 'Маркина', 'Уборщик', '10', 10000, 49);

/*
SELECT * 
FROM `staff` 
ORDER BY age DESC;
*/


/*
Выведите все записи, отсортированные по полю "age" по возрастанию
*/

SELECT * 
FROM `staff` 
ORDER BY age;

/*
Выведите все записи, отсортированные по полю “firstname"
*/

SELECT * 
FROM `staff` 
ORDER BY firstname;

/*
Выведите записи полей "firstname ", “lastname", "age", 
отсортированные по полю "firstname " в алфавитном порядке по убыванию
*/

SELECT `firstname`, `lastname`, `age`
FROM `staff`
ORDER BY firstname DESC;

/*
Выполните сортировку по полям "firstname" и "age" по убыванию
*/

SELECT `firstname`, `age`
FROM `staff`
ORDER BY firstname DESC, age DESC;


/*
1. Выведите уникальные (неповторяющиеся) значения полей "firstname"
*/

SELECT DISTINCT `firstname` AS unikal_name
FROM `staff`;

/*
2. Отсортируйте записи по возрастанию значений поля "id". 
Выведите первые две записи данной выборки
*/

SELECT *
FROM `staff`
ORDER BY id
LIMIT 2;

/*
3. Отсортируйте записи по возрастанию значений поля "id". 
Пропустите первые 4 строки данной выборки и извлеките следующие 3
*/

SELECT *
FROM `staff`
ORDER BY id
LIMIT 3 OFFSET 4;

/*
Задание от преподавателя
или
4. Отсортируйте записи по убыванию поля "id".
Пропустите две строки данной выборки и извлеките 
следующие за ними 3 строки
*/

SELECT *
FROM 
(
SELECT * FROM `staff`
ORDER BY Id DESC
LIMIT 3 OFFSET 2
) AS reversed_table
ORDER BY Id;
-- ORDER BY Id As;

/*
1. Найдите количество сотрудников с должностью «Рабочий» 
*/

SELECT *
FROM `staff`
WHERE `post` = "Рабочий";

-- усложняем

SELECT COUNT(*)
FROM `staff`
WHERE `post` = "Рабочий";

/*
2. Посчитайте ежемесячную зарплату начальников
*/

SELECT SUM(`salary`)
FROM `staff`
WHERE `post` = "Начальник";

/*
3. Выведите средний возраст сотрудников, у 
которых заработная плата больше 30000
*/

SELECT AVG(`age`) AS "midl_age_selary"
FROM `staff` 
WHERE `salary` > 30000;

/*
4. Выведите максимальную и минимальную заработные платы
*/

SELECT MAX(`salary`), MIN(`salary`)
FROM `staff`;

-- создаем таблицу
CREATE TABLE `activity_staff`
(
`id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
`staff_id` INT UNSIGNED,
`date_activity` DATE,
`count_page` INT UNSIGNED,
FOREIGN KEY (`staff_id`) REFERENCES `staff`(`id`)
);


INSERT INTO `activity_staff` (`staff_id`, `date_activity`, `count_page`)
VALUES
(1, '2022-01-01', 250),
(2, '2022-01-01', 220),
(3, '2022-01-01', 170),
(1, '2022-01-02', 100),
(2, '2022-01-02', 220),
(3, '2022-01-02', 300),
(7, '2022-01-02', 350),
(1, '2022-01-03', 168),
(2, '2022-01-03', 62),
(3, '2022-01-03', 84);

SELECT * 
FROM `activity_staff`;

/*
1. Выведите общее количество напечатанных страниц каждым сотрудником
*/

SELECT `staff_id`, SUM(`count_page`) AS SYMMA
FROM `activity_staff`
GROUP BY `staff_id`;

/*
Сделали ошибку специально:
*/

SELECT `staff_id`, SUM(`count_page`) AS SYMMA , `id`
FROM `activity_staff`
GROUP BY `staff_id`;

/*
2. Посчитайте количество страниц за каждый день
*/

SELECT `date_activity`, SUM(`count_page`)
FROM `activity_staff`
GROUP BY `date_activity`;

/*
3. Найдите среднее арифметическое по количеству ежедневных страниц
*/

SELECT `date_activity`, AVG(`count_page`)
FROM `activity_staff`
GROUP BY `date_activity`;

/*
Сгруппируйте данные о сотрудниках по возрасту: 
1 группа – младше 20 лет
2 группа – от 20 до 40 лет
3 группа – старше  40 лет 
Для каждой группы найдите суммарную зарплату
*/

SELECT
CASE
WHEN `age` < 20 then "младше 20 лет"
WHEN `age` between 20 and 40 then "от 20 до 40 лет"
WHEN `age` > 40 then "старше  40 лет"
ELSE "что - то пошло не так !"
END AS resalt, SUM(`salary`) AS SUM_SALARY
FROM `staff`
GROUP BY resalt;

/*
1. Выведите id сотрудников, которые напечатали более 500 страниц за все дни
*/

SELECT `staff_id`, SUM(`count_page`)
FROM `activity_staff`
GROUP BY `staff_id`HAVING SUM(`count_page`) > 500;

/*
2.  Выведите  дни, когда работало более 3 сотрудников 
Также укажите кол-во сотрудников, которые работали в выбранные дни.
*/

SELECT `date_activity`, COUNT(*) AS "Количество"
FROM `activity_staff`
GROUP BY `date_activity` HAVING COUNT(*) > 3;

SELECT `date_activity`, COUNT(*) AS resalt
FROM `activity_staff`
GROUP BY `date_activity` HAVING resalt > 3;

/*
3. Выведите среднюю заработную плату по должностям, 
которая составляет более 30000
*/

SELECT `post`, AVG(`salary`) AS resalt
FROM `staff`
GROUP BY `post` HAVING AVG(`salary`) > 30000;


SELECT `post`, ROUND(AVG(`salary`), 2) AS resalt
FROM `staff`
GROUP BY `post` HAVING resalt > 30000;