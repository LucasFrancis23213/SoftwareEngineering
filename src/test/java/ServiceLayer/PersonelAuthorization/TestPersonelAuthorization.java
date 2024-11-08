package ServiceLayer.PersonelAuthorization;

import Utilities.Enums.Roles;
import Utilities.Enums.TeachingActivity;
import Utilities.Enums.UserAndAccountActivity;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class TestPersonelAuthorization {
    @Test
    public void TestSystemManagerPermissions(){
        Personel SystemManager = PersonelFactory.CreatePersonel(Roles.SYSTEM_MANAGER);
        Assertions.assertTrue(SystemManager.CheckPermission(UserAndAccountActivity.CREATE_ACCOUNT));
        Assertions.assertFalse(SystemManager.CheckPermission(TeachingActivity.PARTICIPATE_PROJECT));
    }

    @Test
    public void testResponsibleTeacherPermissions() {
        Personel responsibleTeacher = PersonelFactory.CreatePersonel(Roles.RESPONSIBLE_TEACHER);

        // Check permissions for Responsible Teacher
        Assertions.assertTrue(responsibleTeacher.CheckPermission(TeachingActivity.SETUP_COURSE));
        Assertions.assertFalse(responsibleTeacher.CheckPermission(UserAndAccountActivity.CREATE_ACCOUNT));
    }

    @Test
    public void testStudentPermissions() {
        Personel student = PersonelFactory.CreatePersonel(Roles.STUDENT);

        // Check permissions for Student
        Assertions.assertTrue(student.CheckPermission(TeachingActivity.UPLOAD_ASSIGNMENT));
        Assertions.assertFalse(student.CheckPermission(UserAndAccountActivity.DELETE_ACCOUNT));
    }
}
