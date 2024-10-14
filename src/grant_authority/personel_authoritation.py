import os
import sys
# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Utilities.enums import TeachingActivaties, UserAndAccountManagement, Roles
from logger import logger

# 已通过代码测试

class Personel():
    def __init__(self, role_name:Roles, teaching_permission:set, account_management:set) -> None:
        self.role_name:Roles = role_name
        self.teaching_permission:set = teaching_permission
        self.account_management:set = account_management
    
    def check_permission(self, permission) -> bool:
        return permission in self.account_management or permission in self.teaching_permission

class PersonalFactory:
    """
    使用工厂模式新建四种角色
    Returns:
        _type_: _description_
    """
    @staticmethod
    def create_personel(role: Roles) -> Personel:
        if role == Roles.STUDENT:
            # 创建 学生
            teaching_permission = {
                TeachingActivaties.PARTICIPATE_PROJECT,
                TeachingActivaties.UPLOAD_ASSIGNMENT,
                TeachingActivaties.DOWNLOAD_ASSIGNMENT
            }
            account_permission = {
                UserAndAccountManagement.EDIT_ACCOUNT_INFO
            }
            return Personel(role_name=role, teaching_permission=teaching_permission, account_management=account_permission)
        
        elif role == Roles.TEACHER:
            # 创建 老师
            teaching_permission = {
                TeachingActivaties.PUBLISH_PROJECT,
                TeachingActivaties.GRADE_ASSIGNMENT,
                TeachingActivaties.PARTICIPATE_PROJECT,
                TeachingActivaties.UPLOAD_ASSIGNMENT,
                TeachingActivaties.DOWNLOAD_ASSIGNMENT
            }
            account_permission = {
                UserAndAccountManagement.EDIT_ACCOUNT_INFO
            }
            return Personel(role_name=role, teaching_permission=teaching_permission, account_management=account_permission)
        
        elif role == Roles.RESPONSIBLE_TEACHER:
            # 创建 责任教师
            teaching_permission = {
                TeachingActivaties.SETUP_COURSE,
                TeachingActivaties.CLOSE_COURSE,
                TeachingActivaties.MANAGE_GRADE,
                TeachingActivaties.PUBLISH_PROJECT,
                TeachingActivaties.GRADE_ASSIGNMENT,
                TeachingActivaties.PARTICIPATE_PROJECT,
                TeachingActivaties.UPLOAD_ASSIGNMENT,
                TeachingActivaties.DOWNLOAD_ASSIGNMENT
            }
            account_permission = {
                UserAndAccountManagement.EDIT_ACCOUNT_INFO
            }
            return Personel(role_name=role, teaching_permission=teaching_permission, account_management=account_permission)
        
        elif role == Roles.SYSTEM_MANAGER:
            # 创建 系统管理员
            teaching_permission = set()
            account_permission = {
                UserAndAccountManagement.ACTIVATE_ACCOUNT,
                UserAndAccountManagement.ASSIGN_ACCOUNT_PERMISSION,
                UserAndAccountManagement.CREATE_ACCOUNT,
                UserAndAccountManagement.DELETE_ACCOUNT,
                UserAndAccountManagement.EDIT_ACCOUNT_INFO,
                UserAndAccountManagement.VERIFY_NEW_USER
            }
            return Personel(role_name=role, teaching_permission=teaching_permission, account_management=account_permission)
        
        else:
            logger.error("unknown Personel role appeared")
            return None

# sample usage
# if __name__ == '__main__':
#     # 创建系统管理员对象
#     system_manager = PersonalFactory.create_personel(Roles.SYSTEM_MANAGER)
#     print(system_manager.check_permission(UserAndAccountManagement.CREATE_ACCOUNT))  # True
#     print(system_manager.check_permission(TeachingActivaties.PARTICIPATE_PROJECT))  # False

#     # 创建责任教师对象
#     responsible_teacher = PersonalFactory.create_personel(Roles.RESPONSIBLE_TEACHER)
#     print(responsible_teacher.check_permission(TeachingActivaties.SETUP_COURSE))  # True
#     print(responsible_teacher.check_permission(UserAndAccountManagement.CREATE_ACCOUNT))  # False

#     # 创建学生对象
#     student = PersonalFactory.create_personel(Roles.STUDENT)
#     print(student.check_permission(TeachingActivaties.UPLOAD_ASSIGNMENT))  # True
#     print(student.check_permission(UserAndAccountManagement.DELETE_ACCOUNT))  # False
            
            


    
