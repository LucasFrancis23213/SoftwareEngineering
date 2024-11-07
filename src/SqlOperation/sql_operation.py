import sys
import os
# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Utilities.data_classes import Student, Identity
from sqlalchemy import and_,Result
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select


from session_manager import get_session
from logger import logger

import asyncio



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
                    select(Student).filter_by(studentID=student_id)
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
                    select(Student).filter_by(studentID=student_id)
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
                # 使用 select() 来查询
                stmt = select(Student).filter_by(studentID=student_id)
                result: Result = await session.execute(stmt)
                student: Student = result.scalars().first()

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
                # 使用 select() 和 join() 进行联表查询
                stmt = (
                    select(Identity, Student)
                    .join(Student, Identity.userName == Student.studentName)
                )
                result: Result = await session.execute(stmt)
                results = result.all()  # 直接获取所有结果

                for identity, student in results:
                    logger.info(
                        f'Identity 用户名: {identity.userName}, Student 名字: {student.studentName}, StudentID: {student.studentID}')

        except SQLAlchemyError as e:
            logger.error(f'联表查询操作失败, 错误: {e}')
        except Exception as e:
            logger.error(f'发生未预料到的错误: {e}')

# 测试完毕
if __name__ == "__main__":
    async def main():
        crud_sample = CrudSample()

        # 1. 插入操作
        await crud_sample.insert_operation(student_name="张三", student_id="2024001")

        # 2. 查询操作
        student = await crud_sample.query_operation(student_id="2024001")
        if student:
            print(f'查询成功: {student.studentName}, ID: {student.studentID}')

        # 3. 更新操作
        await crud_sample.update_operation(student_id="2024001", new_name="李四")

        # 4. 查询更新后的学生
        updated_student = await crud_sample.query_operation(student_id="2024001")
        if updated_student:
            print(f'更新后的学生: {updated_student.studentName}, ID: {updated_student.studentID}')

        # 5. 删除操作
        await crud_sample.delete_operation(student_id="2024001")

        # 6. 验证删除
        deleted_student = await crud_sample.query_operation(student_id="2024001")
        if deleted_student is None:
            print('学生已成功删除。')

        # 7. 联表查询操作
#        await crud_sample.join_operation()


    asyncio.run(main())