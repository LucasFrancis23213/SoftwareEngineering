from Utilities.data_classes import Student, Identity
from sqlalchemy import and_,Result
from sqlalchemy.exc import SQLAlchemyError

from session_manager import get_session
from logger import logger

# this file shows the sample of basic crud operation 
# please notice that these samples DID NOT CONTAIN CONNECT TO DATABASE OPERATION!!!
class CrudSample:
    async def insert_operation(self, student_name: str, student_id: str):
        """
        插入操作样例
        Args:
            student_name (str): 学生姓名
            student_id (str): 学生ID
        """
        try:
            async with get_session() as session:  # 自动管理session
                new_student = Student(studentName=student_name, studentID=student_id)
                session.add(new_student)
                logger.info(f'插入成功: {student_name} ({student_id})')
        except SQLAlchemyError as e:
            logger.error(f'插入失败: {student_name} ({student_id}), 错误: {e}')
        except Exception as e:
            logger.error(f'发生未预料到的错误: {e}')

    async def delete_operation(self, student_id: str):
        """
        删除操作样例
        Args:
            student_id (str): 学生ID
        """
        try:
            async with get_session() as session:  # 自动管理session
                result:Result = await session.execute(
                    session.query(Student).filter_by(studentID=student_id)
                )
                student = result.scalars().first()
                if student:
                    await session.delete(student)
                    logger.info(f'删除成功: {student.studentName} ({student.studentID})')
                else:
                    logger.info(f'未找到匹配的学生ID: {student_id}')
        except SQLAlchemyError as e:
            logger.error(f'删除操作失败, 错误: {e}')
        except Exception as e:
            logger.error(f'发生未预料到的错误: {e}')

    async def update_operation(self, student_id: str, new_name: str):
        """
        更新操作样例
        Args:
            student_id (str): 学生ID
            new_name (str): 新名字
        """
        try:
            async with get_session() as session:  # 自动管理session
                result:Result = await session.execute(
                    session.query(Student).filter_by(studentID=student_id)
                )
                student = result.scalars().first()
                if student:
                    student.studentName = new_name
                    logger.info(f'更新成功: {student_id} 更新为新名字 {new_name}')
                else:
                    logger.info(f'未找到学生ID: {student_id}')
        except SQLAlchemyError as e:
            logger.error(f'更新操作失败, 错误: {e}')
        except Exception as e:
            logger.error(f'发生未预料到的错误: {e}')

    async def query_operation(self, student_id: str) -> Student:
        """
        查询操作样例
        Args:
            student_id (str): 学生ID
        Returns:
            Student: 查询到的学生对象或 None
        """
        try:
            async with get_session() as session:  # 自动管理session
                result:Result = await session.execute(
                    session.query(Student).filter_by(studentID=student_id)
                )
                student:Student = result.scalars().first()
                if student:
                    logger.info(f'找到学生: {student.studentName}, ID: {student.studentID}')
                    return student
                else:
                    logger.info(f'未找到学生ID: {student_id}')
                    return None
        except SQLAlchemyError as e:
            logger.error(f'查询操作失败, 错误: {e}')
            return None
        except Exception as e:
            logger.error(f'发生未预料到的错误: {e}')
            return None

    async def join_operation(self):
        """
        联表查询操作样例
        """
        try:
            async with get_session() as session:  # 自动管理session
                result:Result = await session.execute(
                    session.query(Identity, Student).join(Student, Identity.userName == Student.studentName)
                )
                results = result.scalars().all()
                for identity, student in results:
                    logger.info(f'Identity 用户名: {identity.userName}, Student 名字: {student.studentName}, StudentID: {student.studentID}')
        except SQLAlchemyError as e:
            logger.error(f'联表查询操作失败, 错误: {e}')
        except Exception as e:
            logger.error(f'发生未预料到的错误: {e}')