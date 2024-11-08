package ServiceLayer.PersonelAuthorization;

import Utilities.Enums.*;
import java.util.Set;

public class Personel {
    private Roles PersonelRole;
    private Set<TeachingActivity> TeachingPermission;
    private Set<UserAndAccountActivity> AccountPermission;

    public Personel(Roles role, Set<TeachingActivity> teaching, Set<UserAndAccountActivity> account){
        this.PersonelRole = role;
        this.AccountPermission = account;
        this.TeachingPermission = teaching;
    }

    public boolean CheckPermission(Enum<?> permission){
        return this.TeachingPermission.contains(permission) || this.AccountPermission.contains(permission);
    }
}
