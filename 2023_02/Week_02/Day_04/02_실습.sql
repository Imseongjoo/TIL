-- 문제 1
-- 테이블 products 에서 평균 MSRP 보다 큰 product 의 productCode , productName , MSRP 를 조회하시오.
-- 단, MSRP 기준 오름차순으로 정렬하세요.
SELECT
  productCode,
  productName,
  MSRP
FROM
  products
WHERE
  MSRP > (
    SELECT
      AVG(MSRP)
    FROM
      products
  )
ORDER BY
  MSRP ASC;

-- 문제 2
-- 테이블 customers 에서 2003년 1월 6일과 2003년 3월 26일 사이에 주문(order)을 한 고객의 customerNumber, customerName 를 조회하시오.
-- 단, customerNumber 기준 오름차순으로 정렬하세요.
SELECT
  customerNumber,
  customerName
FROM
  customers
WHERE
  customerNumber IN (
    SELECT
      customerNumber
    FROM
      orders
    WHERE
      orderDate BETWEEN '2003-01-06' AND '2003-03-26'
  )
ORDER BY
  customerNumber ASC;

-- 문제 3
-- productLine 가 Classic Cars 인 제품(product) 중 MSRP가 가장 큰 제품의 productCode , productName , productLine , MSRP 를 조회하시오.
-- 제품 데이터는 products 테이블을 활용합니다.
SELECT
  productCode,
  productName,
  productLine,
  MSRP
FROM
  products
WHERE
  productLine = 'Classic Cars'
ORDER BY
  MSRP DESC
LIMIT
  1;

-- 문제 4
-- 가장 많은 고객(customer)이 사는 나라(country)의 customerNumber , customerName , country 를 조회하시오.
-- 고객 데이터는 customers 테이블을 활용합니다.
-- 단, customerNumber 기준 오름차순으로 정렬하세요.
SELECT
  c.customerNumber,
  c.customerName,
  c.country
FROM
  customers c
WHERE
  c.country = (
    SELECT
      country
    FROM
      customers
    GROUP BY
      country
    ORDER BY
      COUNT(*) DESC
    LIMIT
      1
  )
ORDER BY
  c.customerNumber ASC;

-- 문제 5
-- 가장 많은 주문(order)을 한 고객(customer)의 customerNumber , customerName , 주문 수(order_count) 를 조회하시오.
-- 고객 데이터는 customers 테이블, 주문 테이블은 orders 테이블을 활용합니다.
SELECT
  c.customerNumber,
  c.customerName,
  COUNT(o.orderNumber) as order_count
FROM
  customers c
  JOIN orders o ON c.customerNumber = o.customerNumber
GROUP BY
  c.customerNumber
ORDER BY
  order_count DESC
LIMIT
  1;

-- 문제 6
-- 주문 날짜(orderDate)가 2004년인 주문(orderdetail) 제품(product)의 productCode , productName 를 조회하시오.
-- 주문 날짜 데이터는 orders 테이블, 주문 - 제품 데이터는 orderdetails 테이블, 제품 데이터는 products 테이블을 활용합니다.
SELECT
  p.productCode,
  p.productName
FROM
  products p
  JOIN orderdetails od ON p.productCode = od.productCode
  JOIN orders o ON od.orderNumber = o.orderNumber
WHERE
  YEAR (o.orderDate) = 2004;