
def is_hospital_admin(user):
    return user.groups.filter(name='admin').exists()


def is_department_admin(user):
    return user.groups.filter(name='department-admin').exists()


def is_hospital_staff(user):
    return user.groups.filter(name='staff').exists()
