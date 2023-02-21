CREATE TABLE Lecture (
    LectureID INT PRIMARY KEY,
    LectureName VARCHAR(50),
    LectureDescription TEXT,
    InstructorName VARCHAR(50),
    LectureDate DATE,
    CourseID INT
);

CREATE TABLE Assignment (
    AssignmentID INT PRIMARY KEY,
    AssignmentName VARCHAR(50),
    AssignmentDescription TEXT,
    AssignmentDeadline DATE,
    LectureID INT,
    CONSTRAINT fk_LectureID FOREIGN KEY (LectureID)
        REFERENCES Lecture (LectureID)
);

CREATE TABLE Survey (
    SurveyID INT PRIMARY KEY,
    SurveyName VARCHAR(50),
    SurveyDescription TEXT,
    SurveyDeadline DATE,
    AssignmentID INT,
    CONSTRAINT fk_AssignmentID FOREIGN KEY (AssignmentID)
        REFERENCES Assignment (AssignmentID)
);