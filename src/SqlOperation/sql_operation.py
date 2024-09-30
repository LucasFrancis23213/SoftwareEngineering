from Utilities.data_classes import Student, Identity
from sqlalchemy import and_

from session_manager import get_session
from logger import logger

# this file shows the sample of basic crud operation 
# please notice that these samples DID NOT CONTAIN CONNECT TO DATABASE OPERATION!!!
class crud_sample:
    def __init__(self) -> None:
        with get_session() as session:
            self.session = session
        
    def insert_operation(self):
        """
        insert operation sample
        """
        try:
            new_student = Student(studentName="John Doe", studentID="1234567")
            self.session.add(new_student)
            logger.info('insert operation succeed')
        except:
            logger.warning(f'insert student {new_student.studentName} {new_student.studentID} failed')
    
    def delete_operation(self, studentID):
        """
        delete operation sample
        Args:
            studentID (str): student id
        """
        try:
            student = self.session.query(Student).filter_by(studentID=studentID).first()
            if student:
                self.session.delete(student)
                logger.info(f'found and deleted student {student.studentName} {student.studentID}')
            else:
                logger.info(f'did not find student match restriction: studentID = {studentID}')
        except Exception as e:
            self.session.rollback()
            logger.warning(f'delete operation failed, error is {e}')
        
    def update_operation(self, studentID, new_name):
        """
        update operation sample
        Args:
            studentID (str): 
            new_name (str): 
        """
        try:
            student = self.session.query(Student).filter_by(studentID=studentID).first()
            if student:
                student.studentName = new_name
                logger.info(f'Student {studentID} updated to new name {new_name}')
            else:
                logger.info(f'No student found with ID {studentID}')
        except Exception as e:
            self.session.rollback()
            logger.warning(f'Update operation failed: {e}')
            
    def query_operation(self, studentID) -> Student:
        """
        query operation sample
        Args:
            studentID (str): 
        Returns:
            Student: 
        """
        student = self.session.query(Student).filter(
            and_(
                Student.studentID == '1234567',
                Student.studentName == 'John'
            )).first()
        if student:
            logger.info(f'Student found: {student.studentName}, ID: {student.studentID}')
            return student
        else:
            logger.info(f'No student found with ID {studentID}')
            return None
    def join_operation(self):
        """
        join opertaion sample
        """
        results = self.session.query(Identity, Student).join(Student, Identity.userName == Student.studentName).all()
        
        for identity, student in results:
            print(f"Identity userName: {identity.userName}, Student studentName: {student.studentName}, StudentID: {student.studentID}")