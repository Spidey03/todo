from django.shortcuts import redirect, render


def add_task(request):
    from todolist.models import Category
    categories = Category.objects.all()
    return render(request, "add_task.html", {'categories': categories})