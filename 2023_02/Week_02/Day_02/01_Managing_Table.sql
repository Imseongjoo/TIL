CREATE TABLE examples (
	examID INT AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    PRIMARY KEY (examID)
);

SHOW COLUMNS FROM examples;

DROP TABLE examples;

ALTER TABLE
	examples
ADD
	country VARCHAR(100) NOT NULL;
    
ALTER TABLE examples
ADD 
	(age INT NOT NULL,
	address VARCHAR(100) NOT NULL);
    
ALTER TABLE 
	examples
MODIFY
	address VARCHAR(50) NOT NULL;
    
ALTER TABLE examples
MODIFY lastName VARCHAR(10) NOT NULL,
MODIFY firstName VARCHAR(10) NOT NULL;

ALTER TABLE
	examples
CHANGE COLUMN
	country state VARCHAR(100) NOT NULL;

ALTER TABLE
	examples
CHANGE COLUMN
	state kdt INT NOT NULL;
    
ALTER TABLE
	examples
DROP COLUMN
	address;
    
ALTER TABLE examples
DROP COLUMN state, 
DROP COLUMN age;