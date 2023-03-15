-- 문제 1
-- 필드 정보를 참고해서 테이블 users 를 생성하시오.
-- 필드 정보
-- Field	Type	Null	Key	Default	Extra
-- userId	int	NO	PRI	NULL	auto_increment
-- first_name	varchar(20)	NO		NULL	
-- last_name	varchar(20)	NO		NULL	
-- birthday	date	NO		NULL	
-- city	varchar(100)	YES		NULL	
-- country	varchar(100)	YES		NULL	
-- email	varchar(100)	YES		NULL	
-- created_at	datetime	YES		CURRENT_TIMESTAMP	DEFAULT_GENERATED
CREATE TABLE
    users (
        userId INT NOT NULL AUTO_INCREMENT,
        firstusersuserIdfirst_namelast_name_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        birthday date NOT NULL,
        city VARCHAR(100),
        country VARCHAR(100),
        email VARCHAR(100),
        created_at DATETIME NOT NULL DEFAULT now (),
        PRIMARY KEY (userId)
    );

-- 문제 2
-- 레코드 정보를 보고 테이블 users 에 데이터를 입력하시오.
-- 레코드 정보
-- first_name	last_name	birthday	city	country	email
-- Beemo	Jeong	1000-01-01			beemo@hphk.kr
-- Jieun	Lee	1993-05-16	Seoul	Korea	
-- Dami	Kim	1995-04-09	Seoul	Korea	
-- Kwangsoo	Lee	1985-07-14	Seoul	Korea	
INSERT INTO
    users (
        first_name,
        last_name,
        birthday,
        city,
        country,
        email
    )
VALUES
    (
        'Beemo',
        'Jeong',
        '1000-01-01',
        NULL,
        NULL,
        'beemo@hphk.kr'
    ),
    (
        'Jieun',
        'Lee',
        '1993-05-16',
        'Seoul',
        'Korea',
        NULL
    ),
    (
        'Dami',
        'Kim',
        '1995-04-09',
        'Seoul',
        'Korea',
        NULL
    ),
    (
        'Kwangsoo',
        'Lee',
        '1985-07-14',
        'Seoul',
        'Korea',
        NULL
    );

-- 문제 3
-- 테이블 users 에 임의로 데이터 5개를 입력하시오.
INSERT INTO
    users (
        first_name,
        last_name,
        birthday,
        city,
        country,
        email
    )
VALUES
    (
        'first_name1',
        'last_name1',
        '1000-01-01',
        NULL,
        NULL,
        NULL
    ),
    (
        'first_name2',
        'last_name2',
        '1000-01-01',
        NULL,
        NULL,
        NULL
    ),
    (
        'first_name3',
        'last_name3',
        '1000-01-01',
        NULL,
        NULL,
        NULL
    ),
    (
        'first_name4',
        'last_name4',
        '1000-01-01',
        NULL,
        NULL,
        NULL
    ),
    (
        'first_name5',
        'last_name5',
        '1000-01-01',
        NULL,
        NULL,
        NULL
    );

-- 문제 4
-- 2번 레코드의 first_name, last_name, birthday 필드 값을 자신의 이름, 성, 생년월일로 변경하시오.
UPDATE users
SET
    first_name = 'Seongjoo',
    last_name = 'Lim',
    birthday = '1994-12-28'
WHERE
    userId = 2;

-- 문제 5
-- 테이블 users 에서 country 필드가 NULL 인 모든 레코드의 country 필드 값을 Korea 로 변경하시오.
UPDATE users
SET
    country = 'Korea'
WHERE
    country IS NULL;

-- 문제 6
-- 테이블 users 에서 first_name 필드가 Beemo 인 레코드를 삭제하시오.
DELETE FROM users
WHERE
    first_name = 'Beemo';

-- 문제 7
-- 테이블 users 에서 first_name 필드가 Kwangsoo, last_name 필드가 Lee 인 레코드를 삭제하시오.
DELETE FROM users
WHERE
    irst_name = 'Kwangsoo'
    and last_name = 'Lee';

-- 문제 8
-- 테이블 users 에서 가장 나중에 생성한 레코드 1개를 삭제하시오.
DELETE FROM users
ORDER BY
    created_at DESC
LIMIT
    1;