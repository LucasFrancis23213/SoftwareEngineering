from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from SqlOperation.db_config import config
from contextlib import contextmanager

from logger import logger
from Utilities.data_classes import Student
from main import Database_URL


engine = create_engine(url=Database_URL)
Session = sessionmaker(bind=engine)

@contextmanager
def get_session():
    session = Session()
    try:
        # yield 关键字在这里将会话对象传递给 with 语句中的代码块。
        # 此时，用户可以在 with 语句中使用这个会话对象执行数据库操作
        yield session
        session.commit()
        logger.info('successfully create session')
    except Exception as e:
        session.rollback()
        logger.error(f'create session failed, error is {e}, rolling back now')
        raise
    finally:
        session.close()
        logger.info('sessio has been closed')

def sample():
    """
    sample of using function get_session()
    """
    with get_session() as session:
        new_student = Student(studentName="John Doe", studentID="1234567")
        session.add(new_student)
        students = session.query(Student).all()
        for student in students:
            print(f"Student Name: {student.studentName}, Student ID: {student.studentID}")
