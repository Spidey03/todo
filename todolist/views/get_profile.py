from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
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
    return Response(response)


