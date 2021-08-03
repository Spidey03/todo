def get_user_details(user_id: int):
    from todolist.models import User
    user = User.objects.values().get(id=user_id)
    from todolist.dtos.dtos import UserDTO
    user_dto = UserDTO(
        id=user['id'],
        username=user['username'],
        email=user['email'],
        bio=user['bio'],
        firstname=user['first_name'],
        lastname=user['last_name'],
        profile_pic=user['profile_pic']
    )
    return user_dto


def get_all_labels():
    from todolist.models import Label
    lables = Label.objects.values()
    lable_dtos = get_lable_dtos(lables)
    return lable_dtos


def get_all_categories():
    from todolist.models import Category
    categories = Category.objects.values()
    category_dtos = get_category_dtos(categories)
    return category_dtos


def get_lable_dtos(lables):
    from todolist.dtos.dtos import LableDTO
    lable_dtos = [
        LableDTO(id=lable['id'], name=lable['name'])
        for lable in lables]
    return lable_dtos


def get_category_dtos(categories):
    from todolist.dtos.dtos import CategoryDTO
    category_dtos = [
        CategoryDTO(id=category['id'], name=category['name'])
        for category in categories
    ]
    return category_dtos
