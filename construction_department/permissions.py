def is_construction_user(user):
    return user.groups.filter(name='ConstructionGroup').exists()
