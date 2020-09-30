from django.shortcuts import render, redirect


def login(request):
    if request.user.is_authenticated:
        return redirect('/tasks')
    return render(request, "login.html",)
