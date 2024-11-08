package ServiceLayer.PersonelAuthorization;

import Utilities.Enums.*;

import java.util.EnumSet;

public class PersonelFactory {
    public static Personel CreatePersonel(Roles role){
        switch (role){
            case STUDENT:
                return new Personel(
                        Roles.STUDENT,
                        EnumSet.of(
                                TeachingActivity.PARTICIPATE_PROJECT,
                                TeachingActivity.UPLOAD_ASSIGNMENT,
                                TeachingActivity.DOWNLOAD_ASSIGNMENT),
                        EnumSet.of(
                             UserAndAccountActivity.EDIT_ACCOUNT_INFO
                        ));
            case TEACHER:
                return new Personel(
                        Roles.TEACHER,
                        EnumSet.of(
                                TeachingActivity.PUBLISH_PROJECT,
                                TeachingActivity.GRADE_ASSIGNMENT,
                                TeachingActivity.PARTICIPATE_PROJECT,
                                TeachingActivity.UPLOAD_ASSIGNMENT,
                                TeachingActivity.DOWNLOAD_ASSIGNMENT
                        ),
                        EnumSet.of(
                                UserAndAccountActivity.EDIT_ACCOUNT_INFO
                        ));
            case RESPONSIBLE_TEACHER:
                return new Personel(
                        Roles.RESPONSIBLE_TEACHER,
                        EnumSet.of(
                                TeachingActivity.SETUP_COURSE,
                                TeachingActivity.CLOSE_COURSE,
                                TeachingActivity.MANAGE_GRADE,
                                TeachingActivity.PUBLISH_PROJECT,
                                TeachingActivity.GRADE_ASSIGNMENT,
                                TeachingActivity.PARTICIPATE_PROJECT,
                                TeachingActivity.UPLOAD_ASSIGNMENT,
                                TeachingActivity.DOWNLOAD_ASSIGNMENT
                        ),
                        EnumSet.of(
                                UserAndAccountActivity.EDIT_ACCOUNT_INFO
                        ));
            case SYSTEM_MANAGER:
                return new Personel(
                        Roles.SYSTEM_MANAGER,
                        EnumSet.noneOf(TeachingActivity.class),
                        EnumSet.of(
                                UserAndAccountActivity.ACTIVATE_ACCOUNT,
                                UserAndAccountActivity.ASSIGN_ACCOUNT_PERMISSION,
                                UserAndAccountActivity.CREATE_ACCOUNT,
                                UserAndAccountActivity.DELETE_ACCOUNT,
                                UserAndAccountActivity.EDIT_ACCOUNT_INFO,
                                UserAndAccountActivity.VERIFY_NEW_USER
                        ));
            default:
                throw new IllegalArgumentException("unknown Personel role");
        }
    }
}
