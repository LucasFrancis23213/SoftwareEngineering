from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager, asynccontextmanager

from logger import logger
from Utilities.data_classes import Student
from main import Database_URL

# 创建异步引擎
engine = create_async_engine(url=Database_URL, echo=True, future=True)

# 创建一个异步的 session 工厂
AsyncSessionFactory = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# engine = create_engine(url=Database_URL)
# Session = sessionmaker(bind=engine)

@asynccontextmanager
async def get_session():
    session = AsyncSessionFactory()
    try:
        yield session  # 将 session 传递给 with 语句
        await session.commit()  # 异步提交事务
        logger.info('Async session commit succeeded')
    except Exception as e:
        await session.rollback()  # 异步回滚事务
        logger.error(f'Async session commit failed, rolling back. Error: {e}')
        raise
    finally:
        await session.close()  # 异步关闭 session
        logger.info('Async session has been closed')

async def sample():
    """
    sample of using function get_session()
    """
    async with get_session() as session:
        new_student = Student(studentName="John Doe", studentID="1234567")
        session.add(new_student)
        students = session.query(Student).all()
        for student in students:
            print(f"Student Name: {student.studentName}, Student ID: {student.studentID}")
