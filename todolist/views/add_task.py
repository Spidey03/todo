from rest_framework.response import Response


def add_task(request):
    if request.method == 'POST':
        details = request.POST
        title = details['title']
        content = details['content']
        date = details['date']
        category = details.get('category', None)
        label = details.get('label', 'Home')

        from todolist.presenters.presenter_implementation import \
            PresenterImplementation
        from todolist.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()
        presenter = PresenterImplementation()
        from todolist.interactors.add_task import AddNewTask
        interactor = AddNewTask(storage=storage, presenter=presenter)

        response = interactor.add_new_task_wrapper(
            title=title, content=content, date=date, category=category,
            label=label
        )

        return Response(response)
