from rest_framework.response import Response

from todolist.constants import constants


def create_user_dto(username, firstname, lastname, email, bio, password1,
                    password2, profile_pic):
    from todolist.interactors.dtos import CreateUserDTO
    create_user_dto = CreateUserDTO(username=username, first_name=firstname,
                                    last_name=lastname, email=email, bio=bio,
                                    password1=password1, password2=password2,
                                    profile_pic=profile_pic)
    return create_user_dto


def signup_confirm(request):
    if request.method == 'POST':
        details = request.POST
        username = details['username']
        email = details['email']
        firstname = details['firstname']
        lastname = details['lastname']
        bio = details['bio']
        profile_pic = details['profile_pic']
        print(profile_pic)
        if not profile_pic or profile_pic == "":
            profile_pic = constants.PROFILE_PIC
        print(profile_pic)
        password1 = details['password1']
        password2 = details['password2']
        user_dto = create_user_dto(username=username, firstname=firstname,
                                   lastname=lastname, email=email, bio=bio,
                                   password1=password1, password2=password2,
                                   profile_pic=profile_pic)

        from todolist.storages.storage_implementation import \
            StorageImplementation
        from todolist.presenters.presenter_implementation import \
            PresenterImplementation
        storage = StorageImplementation()
        presenter = PresenterImplementation()
        from todolist.interactors.storages.signup import Signup
        interactor = Signup(storage=storage)

        response = interactor.signup_wrapper(user_dto=user_dto, presenter=presenter)
        return Response(response)