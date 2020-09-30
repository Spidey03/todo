from django.shortcuts import render


def get_profile(request):
    user_id = request.user.id
    from todolist.storages.storage_implementation import StorageImplementation
    from todolist.presenters.presenter_implementation import \
        PresenterImplementation
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    from todolist.interactors.get_profile import GetProfile
    interactor = GetProfile(storage=storage)
    response = interactor.get_profile_details_wrapper(
        user_id=user_id, presenter=presenter)
    context = {
        "title": {
            "name": "Home",
            "url": "/tasks"
        },
        "user": response
    }
    return render(request, "profile.html", context)


