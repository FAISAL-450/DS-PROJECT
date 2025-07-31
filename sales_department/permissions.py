def is_sales_user(user):
    return user.groups.filter(name='SalesGroup').exists()
