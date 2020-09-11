from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, "index.html", {"todos": ['todos','hai'], "categories": ['categories']})



def del_tasks(request):
    if request.method == 'POST':
        checkedlist = request.POST["checkedbox"]
        # TODO: del tasks in db
        return redirect('/todo')
