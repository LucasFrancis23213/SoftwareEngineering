from sqlalchemy import  Column, Integer, String, Text, DateTime, Enum, ForeignKey
from main import Base


class Identity(Base): 
    __tablename__ = "identity"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    userName = Column(String(100))
    userID = Column(String(7))
    IsTeacher = Column(Integer, default = 0)
    email = Column(String) # 没加到database
    status = Column(Enum('activated', 'deactivated'), default='deactivated')

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, autoincrement=True)  # 添加主键
    studentName = Column(String(100), ForeignKey("identity.userName"), nullable=False)
    studentID = Column(String(7), ForeignKey("identity.userID"), nullable=False)
    # email = Column(String, ForeignKey("identity.email"), nullable = False) # 没加到database
    
class Teacher(Base):
    __tablename__ = "teacher"
    
    teacherName = Column(String(100), ForeignKey("identity.userName"), nullable=False)
    teacherID = Column(String(7), ForeignKey("identity.userID"), nullable=False, primary_key=True)
    classID = Column(String(10), ForeignKey("course.courseID"))
    teacherType = Column(Enum("Normal", "Admin", "TeachingAssistance", "SystemManager"), nullable=False)
    email = Column(String, ForeignKey("identity.email"), nullable = False) # 没加到database

class Course(Base):
    __tablename__ = 'course'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    courseName = Column(String(100), nullable=False)
    courseID = Column(String(10), unique=True, nullable=False)

class Login(Base):
    __tablename__ = 'login'
    
    userName = Column(String(100), ForeignKey('identity.userName'))
    userID = Column(String(7), ForeignKey('identity.userID'), primary_key=True, nullable=False)
    # userEmail = Column(String(100), nullable=False) 应该删除
    password = Column(String, nullable=False)

class Assignment(Base):
    __tablename__ = 'assignment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    publisherID = Column(String(7), ForeignKey('teacher.teacherID'), nullable=False)
    assignmentTopic = Column(String(100), nullable=False)
    assignmentContent = Column(Text, nullable=False)
    publishTime = Column(DateTime, nullable=False)
    deadline = Column(DateTime, nullable=False)

class Submission(Base):
    __tablename__ = 'submission'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    studentID = Column(String(7), ForeignKey('student.studentID'), nullable=False)
    assignmentTopic = Column(String(100), ForeignKey('assignment.assignmentTopic'), nullable=False)
    commitTime = Column(DateTime, nullable=False)
    status = Column(Enum('Submitted', 'Graded', 'Late'), nullable=False)
    commitContent = Column(Text)

class Grading(Base):
    __tablename__ = 'grading'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    teacherID = Column(String(20), ForeignKey('teacher.teacherID'), nullable=False)
    submissionID = Column(Integer, ForeignKey('submission.id'), nullable=False)
    gradeTime = Column(DateTime, nullable=False)
    grades = Column(Integer)  # 根据需要定义成绩的类型
  