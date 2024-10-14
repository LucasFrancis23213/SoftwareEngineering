from enum import Enum, auto

class UserAndAccountManagement(Enum):
    CREATE_ACCOUNT = auto()
    VERIFY_NEW_USER = auto()
    ACTIVATE_ACCOUNT = auto()
    ASSIGN_ACCOUNT_PERMISSION = auto()
    EDIT_ACCOUNT_INFO = auto()
    DELETE_ACCOUNT = auto()

class TeachingActivaties(Enum):
    SETUP_COURSE = auto()
    PUBLISH_PROJECT = auto()
    PARTICIPATE_PROJECT = auto()
    UPLOAD_ASSIGNMENT = auto()
    DOWNLOAD_ASSIGNMENT = auto()
    GRADE_ASSIGNMENT = auto()
    MANAGE_GRADE = auto()
    CLOSE_COURSE = auto()

class Roles(Enum):
    STUDENT = auto()
    TEACHER = auto()
    RESPONSIBLE_TEACHER = auto()
    SYSTEM_MANAGER = auto()
    
    