def user_details(user_id: int):
    from todolist.models import User
    user = User.objects.get(id=user_id)
    print(user.__dict__)
    return user
