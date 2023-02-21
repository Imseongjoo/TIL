-- Student Entity
CREATE TABLE student (
  student_id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50),
  major VARCHAR(50)
);

-- Professor Entity
CREATE TABLE professor (
  professor_id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50),
  department VARCHAR(50)
);

-- Course Entity
CREATE TABLE course (
  course_id INT PRIMARY KEY,
  course_code VARCHAR(10),
  course_name VARCHAR(50),
  entity_type ENUM('교양', '전공')
);

-- Course Offering Entity
CREATE TABLE course_offering (
  course_offering_id INT PRIMARY KEY,
  year INT,
  semester ENUM('1학기', '여름학기', '2학기', '겨울학기'),
  professor_id INT,
  course_id INT,
  FOREIGN KEY (professor_id) REFERENCES professor (professor_id),
  FOREIGN KEY (course_id) REFERENCES course (course_id)
);

-- Enrollment Entity
CREATE TABLE enrollment (
  enrollment_id INT PRIMARY KEY,
  student_id INT,
  course_offering_id INT,
  FOREIGN KEY (student_id) REFERENCES student (student_id),
  FOREIGN KEY (course_offering_id) REFERENCES course_offering (course_offering_id)
);