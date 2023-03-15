-- 문제 1
-- 테이블 customers 에서 country 필드의 중복을 제거한 데이터를 조회하시오.
-- 단, country 기준 오름차순으로 정렬하세요.
SELECT DISTINCT
  country
FROM
  customers
ORDER BY
  country ASC;

-- 문제 2
-- 테이블 customers 에서 state 필드의 중복을 제거한 데이터를 조회하시오.
-- 단, state 기준 내림차순으로 정렬하세요.
SELECT DISTINCT
  state
FROM
  customers
ORDER BY
  state DESC;

-- 문제 3
-- 테이블 customers 에서 country 가 USA 가 아닌 customerNumber , customerName , country 필드의 데이터를 조회하시오.
-- 단, customerNumber 기준 내림차순으로 정렬하세요.
SELECT
  customerNumber,
  customerName,
  country
FROM
  customers
WHERE
  country != 'USA'
ORDER BY
  customerNumber DESC;

-- 문제 4
-- 테이블 offices 에서 city 가 Paris 인 데이터를 조회하시오.
SELECT
  *
FROM
  offices
WHERE
  city = 'paris';

-- 문제 5
-- 테이블 customers 에서 country 가 USA 고, state 가 CA 인 customerNumber , customerName , country , state 필드의 데이터를 조회하시오.
-- 단, customerName 기준 내림차순으로 정렬하세요.
SELECT
  customerNumber,
  customerName,
  country,
  state
FROM
  customers
WHERE
  country = 'usa'
  and state = 'CA'
ORDER BY
  customerName DESC;

-- 문제 6
-- 테이블 customers 에서 country 가 USA 고, state 가 CA 또는 NY 인 customerNumber , customerName , country , state 필드의 데이터를 조회하시오.
-- 단, customerNumber 기준 내림차순으로 정렬하세요.
SELECT
  customerNumber,
  customerName,
  country,
  state
FROM
  customers
WHERE
  country = 'usa'
  and state = 'CA'
  or 'NY'
ORDER BY
  customerNumber DESC;

-- 문제 7
-- 테이블 customers 에서 state 가 CA 또는 NY 또는 CT 또는 PA 인 customerNumber , customerName , state 필드의 데이터를 조회하시오.
-- 단, customerNumber 기준 내림차순으로 정렬하세요.
SELECT
  customerNumber,
  customerName,
  state
FROM
  customers
WHERE
  state = 'CA'
  or 'NY'
  or 'CT'
  or 'PA'
ORDER BY
  customerNumber DESC;

-- 문제 8
-- 테이블 products 에서 quantityInStock 가 1000 미만인 productCode , productName , quantityInStock 필드의 데이터를 조회하시오.
-- 단, quantityInStock 기준 오름차순으로 정렬하세요.
SELECT
  productCode,
  productName,
  quantityInStock
FROM
  products
WHERE
  quantityInStock < 1000
ORDER BY
  quantityInStock ASC;

-- 문제 9
-- 테이블 products 에서 quantityInStock 가 2000 과 3000 사이인 productCode , productName , quantityInStock 필드의 데이터를 조회하시오.
-- 단, quantityInStock 기준 내림차순으로 정렬하세요.
SELECT
  productCode,
  productName,
  quantityInStock
FROM
  products
WHERE
  quantityInStock BETWEEN 2000 and 3000
ORDER BY
  quantityInStock DESC;

-- 문제 10
-- 테이블 customers 에서 phone 가 555 로 끝나는 customerNumber , customerName , phone 필드의 데이터를 조회하시오.
-- 단, customerName 기준 내림차순으로 정렬하세요.
SELECT
  customerNumber,
  customerName,
  phone
FROM
  customers
WHERE
  phone LIKE '%555'
ORDER BY
  customerName DESC;

-- 문제 11
-- 테이블 products 에서 quantityInStock 필드가 높은 5개의 productCode , quantityInStock 필드의 데이터를 조회하시오.
SELECT
  productCode,
  quantityInStock
FROM
  products
ORDER BY
  quantityInStock DESC
LIMIT
  5;

-- 문제 12
-- 테이블 employees 에서 jobTitle 필드를 그룹화하여 각 그룹에 대한 개수를 조회하시오.
-- 단, 인원 수 기준 내림차순, jobTitle 기준 내림차순으로 정렬하세요.
SELECT
  jobTitle,
  COUNT(*)
FROM
  employees
GROUP BY
  jobTitle
ORDER BY
  COUNT(*) DESC,
  jobTitle DESC;

-- 문제 13
-- 테이블 customers 에서 country 필드를 그룹화하여 각 그룹에 대한 개수를 조회하시오.
-- 단, 인원 수 기준 내림차순으로 정렬하세요.
SELECT
  country,
  COUNT(*)
FROM
  customers
GROUP BY
  country
ORDER BY
  COUNT(*) DESC,
  country DESC;

-- 문제 14
-- 테이블 orderdetails 에서 orderNumber 필드를 그룹화하여 각 그룹에 대한 quantityOrdered * priceEach 의 합을 조회하시오.
-- 단, quantityOrdered * priceEach 의 합 기준 내림차순으로 정렬하세요.
SELECT
  orderNumber,
  sum(quantityOrdered * priceEach) AS total
FROM
  orderdetails
GROUP BY
  orderNumber
ORDER BY
  total DESC;

-- 문제 15
-- 테이블 orders 에서 년도별(year)로 그룹화하여 orderNumber 필드의 개수를 조회하시오.
SELECT
  YEAR (orderDate),
  COUNT(orderNumber)
FROM
  orders
GROUP BY
  YEAR (orderDate);

-- 문제 16
-- 테이블 products 에서 productLine 필드를 그룹화하여 각 그룹에 대한 quantityInStock 필드의 최댓값을 조회하시오.
-- 단, 최댓값이 9000 미만인 데이터만 조회하시오.
SELECT
  productLine,
  MAX(quantityInStock) AS max_stock
FROM
  products
GROUP BY
  productLine
HAVING
  max_stock < 9000;

-- 문제 17
-- 테이블 orderdetails 에서 ordernumber 필드를 그룹화하여 각 그룹에 대한 quantityOrdered 필드의 합과 priceeach * quantityOrdered 의 합을 조회하시오.
-- 단, quantityOrdered 합이 500 이상, priceeach * quantityOrdered 합이 50000 이상인 데이터만 조회하시오.
SELECT
  orderNumber,
  SUM(quantityOrdered) AS itemsCount,
  SUM(priceeach * quantityOrdered) AS total
FROM
  orderdetails
GROUP BY
  orderNumber
HAVING
  itemsCount >= 500
  AND total >= 50000;