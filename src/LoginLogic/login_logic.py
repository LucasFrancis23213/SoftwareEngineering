import os
import sys
# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlalchemy import and_

from Utilities.data_classes import Login
from SqlOperation.session_manager import get_session
from logger import logger

class LoginManager():
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoginManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, login:Login) -> None:
        self.login = login
    
    def is_password_valid(self) -> {bool, str}:
        try:
            with get_session() as session:
                login_info_in_db = session.query(Login).filter_by(
                    Login.userID == self.login.userID,
                )
            if login_info_in_db:
                if login_info_in_db.password == self.login.password:
                    logger.info('password correct, login succeed')
                    return {True, 'login succeed'}
                else:
                    logger.info('password incorrect')
                    return {False, 'password incorrect'}
            else:
                logger.warning(f'can not find user: {self.login.userName}')
                return {False, 'error: can not find user'}
        except Exception as e:
            logger.error(f'in login_logic.py, error is {str(e)}')
            return {False, f'internal server error, {str(e)}'}