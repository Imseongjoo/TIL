-- 문제 1
-- 필드 정보를 참고해서 테이블 posts 를 생성하시오.
-- 필드 정보
-- Field	Type	Null	Key	Default	Extra
-- postId	int	NO	PRI	NULL	auto_increment
-- title	varchar(50)	NO		NULL	
-- content	varchar(200)	NO		NULL	
SHOW COLUMNS
FROM
	posts;

CREATE TABLE
	posts (
		postId INT AUTO_INCREMENT,
		title VARCHAR(50) NOT NULL,
		content VARCHAR(200) NOT NULL,
		PRIMARY KEY (postId)
	);

-- 문제 2
-- 필드 정보를 보고 테이블 posts 에 새로운 필드를 추가하시오.
-- 필드 정보
-- Field	Type	Null	Key	Default	Extra
-- writer	varchar(100)	YES		Anonymous	
-- created_at	datetime	YES		CURRENT_TIMESTAMP	DEFAULT_GENERATED
ALTER TABLE posts ADD (
	writer VARCHAR(50),
	created_at DATETIME NOT NULL DEFAULT now ()
);

-- 문제 3
-- 필드 정보를 보고 필드 content 의 속성을 아래와 같이 변경하시오.
-- 필드 정보
-- Field	Type	Null	Key	Default	Extra
-- content	text	YES		NULL	
ALTER TABLE posts MODIFY content TEXT;

-- 문제 4
-- 테이블 posts 에서 writer 필드를 삭제하시오.
ALTER TABLE posts
DROP COLUMN writer;

-- 문제 5
-- 테이블 posts 를 삭제하시오.
DROP TABLE posts;

-- 문제 6
-- 테이블 posts 가 존재하지 않으면(NOT EXISTS) 테이블 posts 를 생성하시오.
-- 필드 정보
-- Field	Type	Null	Key	Default	Extra
-- postId	int	NO	PRI	NULL	auto_increment
-- title	varchar(50)	NO		NULL	
-- content	text	NO		NULL	
-- writer	varchar(20)	NO		NULL	
-- created_at	datetime	YES		CURRENT_TIMESTAMP	DEFAULT_GENERATED
CREATE TABLE
	IF NOT EXISTS posts (
		postId INT NOT NULL AUTO_INCREMENT,
		title VARCHAR(50) NOT NULL,
		content text NOT NULL,
		writer VARCHAR(20) NOT NULL,
		created_at DATETIME NOT NULL DEFAULT now (),
		PRIMARY KEY (postId)
	);

-- 문제 7
-- 테이블 posts 가 존재하면 (EXISTS) 테이블 posts 를 삭제하시오.
DROP TABLE IF EXISTS posts;