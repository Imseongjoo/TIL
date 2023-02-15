-- 문제 1
-- 테이블 employees 과 테이블 offices 를 officeCode 기준으로 INNER JOIN 한 데이터를 조회하시오.

-- 조건
-- employeeNumber, lastName, firstName, city 필드만 조회하시오.
-- employeeNumber 기준 오름차순으로 정렬하세요.

SELECT employeeNumber, lastName, firstName, city
FROM employees
INNER JOIN offices
ON employees.officeCode = offices.officeCode
ORDER BY employeeNumber;

-- 문제 2
-- 테이블 customers 와 테이블 offices 를 city 기준으로 LEFT JOIN 한 데이터를 조회하시오.

-- 조건
-- customerNumber , officeCode , 테이블 customers 의 city , 테이블 offices 의 city 필드만 조회하시오.
-- customerNumber 기준 내림차순으로 정렬하세요.

SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
LEFT JOIN offices
ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 문제 3
-- 테이블 customers 와 테이블 offices 를 city 기준으로 RIGHT JOIN 한 데이터를 조회하시오.

-- 조건
-- customerNumber , officeCode , 테이블 customers 의 city , 테이블 offices 의 city 필드만 조회하시오.
-- customerNumber 기준 내림차순으로 정렬하세요.

SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
RIGHT JOIN offices
ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 문제 4
-- 테이블 customers 와 테이블 offices 를 city 기준으로 INNER JOIN 한 데이터를 조회하시오.

-- 조건
-- customerNumber , officeCode , 테이블 customers 의 city , 테이블 offices 의 city 필드만 조회하시오.
-- customerNumber 기준 내림차순으로 정렬하세요.

SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
INNER JOIN offices
ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 문제 5
-- 문제 2, 문제 3, 문제 4 의 조회 결과가 다른 이유를 작성하시오.

-- 문제 6
-- 테이블 customers 와 테이블 offices 를 city 기준으로 FULL OUTER JOIN 한 데이터를 조회하시오.
-- MySQL에서 FULL OUTER JOIN 은 지원하지 않는 기능이므로 MySQL FULL OUTER JOIN 키워드를 검색하여 구현하시오.

-- 조건
-- customerNumber , officeCode , 테이블 customers 의 city , 테이블 offices 의 city 필드만 조회하시오.
-- customerNumber 기준 내림차순으로 정렬하세요.

SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
LEFT JOIN offices ON customers.city = offices.city
UNION
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
RIGHT JOIN offices ON customers.city = offices.city
ORDER BY customerNumber DESC;

SELECT * FROM orderdetails;
SELECT * FROM orders;

-- 문제 7
-- 테이블 orderdetails 와 테이블 orders 를 INNER JOIN 한 데이터를 조회하시오.

-- 조건
-- orderNumber , orderDate 필드만 조회하시오.
-- orderNumber 기준 오름차순으로 정렬하세요.

SELECT orderdetails.orderNumber, orders.orderDate
FROM orderdetails
INNER JOIN orders
ON orderdetails.orderNumber = orders.orderNumber
ORDER BY orderNumber;

-- 문제 8
-- 테이블 orderdetails 와 테이블 products 을 INNER JOIN 한 데이터를 조회하시오.

-- 조건
-- orderNumber , productCode , productName 필드만 조회하시오.
-- orderNumber 기준 오름차순으로 정렬하세요.

SELECT orderdetails.orderNumber, products.productCode, products.productName 
FROM orderdetails
INNER JOIN products
ON orderdetails.productCode = products.productCode
ORDER BY orderNumber;

-- 문제 9
-- 테이블 orderdetails , 테이블 orders , 테이블 products 를 INNER JOIN 한 데이터를 조회하시오.

-- 조건
-- orderNumber , productCode , orderDate, productName 필드만 조회하시오.
-- orderNumber 기준 오름차순으로 정렬하세요.

SELECT orderdetails.orderNumber, orderdetails.productCode, orders.orderDate, products.productName
FROM orderdetails
INNER JOIN orders
ON orderdetails.orderNumber = orders.orderNumber
INNER JOIN products
ON orderdetails.productCode = products.productCode
ORDER BY orderNumber;