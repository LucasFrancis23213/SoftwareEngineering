CREATE TABLE Identity (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userName VARCHAR(100) NOT NULL,
    userID VARCHAR(7) NOT NULL UNIQUE,
    IsTeacher TINYINT DEFAULT 0
);

CREATE TABLE Student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    studentName VARCHAR(100) NOT NULL,
    studentID VARCHAR(7) NOT NULL,
    FOREIGN KEY (studentName) REFERENCES Identity(userName),
    FOREIGN KEY (studentID) REFERENCES Identity(userID)
);

CREATE TABLE Teacher (
    teacherName VARCHAR(100) NOT NULL,
    teacherID VARCHAR(7) NOT NULL PRIMARY KEY,
    classID VARCHAR(10),
    teacherType ENUM('Normal', 'Admin', 'TeachingAssistance') NOT NULL,
    FOREIGN KEY (teacherName) REFERENCES Identity(userName),
    FOREIGN KEY (teacherID) REFERENCES Identity(userID),
    FOREIGN KEY (classID) REFERENCES Course(courseID)  -- 这里假设 Course 表已经存在
);

CREATE TABLE Course (
    id INT AUTO_INCREMENT PRIMARY KEY,
    courseName VARCHAR(100) NOT NULL,
    courseID VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE Login (
    userName VARCHAR(100) NOT NULL,
    userID VARCHAR(7) NOT NULL PRIMARY KEY,
    userEmail VARCHAR(100) NOT NULL,
    FOREIGN KEY (userName) REFERENCES Identity(userName),
    FOREIGN KEY (userID) REFERENCES Identity(userID)
);

CREATE TABLE Assignment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    publisherID VARCHAR(7) NOT NULL,
    assignmentTopic VARCHAR(100) NOT NULL,
    assignmentContent TEXT NOT NULL,
    publishTime DATETIME NOT NULL,
    deadline DATETIME NOT NULL,
    FOREIGN KEY (publisherID) REFERENCES Teacher(teacherID)
);

CREATE TABLE Submission (
    id INT AUTO_INCREMENT PRIMARY KEY,
    studentID VARCHAR(7) NOT NULL,
    assignmentTopic VARCHAR(100) NOT NULL,
    commitTime DATETIME NOT NULL,
    status ENUM('Submitted', 'Graded', 'Late') NOT NULL,
    commitContent TEXT,
    FOREIGN KEY (userID) REFERENCES Student(studentID),
    FOREIGN KEY (assignmentTopic) REFERENCES Assignment(assignmentTopic)
);

CREATE TABLE Grading (
    id INT AUTO_INCREMENT PRIMARY KEY,
    teacherID VARCHAR(7) NOT NULL,
    submissionID INT NOT NULL,
    gradeTime DATETIME NOT NULL,
    grades DECIMAL(5, 2),  -- 根据需要定义成绩的类型
    FOREIGN KEY (teacherID) REFERENCES Teacher(teacherID),
    FOREIGN KEY (submissionID) REFERENCES Submission(id)
);

