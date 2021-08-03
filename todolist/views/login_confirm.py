from rest_framework.decorators import api_view
from rest_framework.response import Response


def login_action(request, username, password):
    from django.contrib.auth import authenticate, login

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return True

@api_view(["POST"])
def login_confirm(request):
    if request.method == 'POST':
        details = request.POST
        username = details['username']
        password = details['password']
        from todolist.storages.storage_implementation import \
            StorageImplementation
        from todolist.presenters.presenter_implementation import \
            PresenterImplementation
        from common.oauth2_storage import OAuth2SQLStorage
        storage = StorageImplementation()
        presenter = PresenterImplementation()
        oauthstorage = OAuth2SQLStorage()
        from todolist.interactors.login import Login
        interactor = Login(storage=storage, oauth_storage=oauthstorage)
        response = interactor.login_wrapper(username=username, password=password,
                                            presenter=presenter)
        return Response(response)


