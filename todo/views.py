from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import TodoList, Profile
from datetime import date
from .forms import ProfilesForm


def signupuser(request):
    if not request.user.is_authenticated and not request.method == 'POST':
        return render(request, 'signup/index.html')

    elif request.method == 'POST' and request.POST['password1'] == request.POST['password2']:
        user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        user.save()
        login(request, user)
        return render(request, 'success.html')
    elif request.method == 'POST' and request.POST['password1'] != request.POST['password2']:
        return render(request, 'signup/index.html')

    elif request.user.is_authenticated:
        return redirect('../todo')


def loginuser(request):
    if not request.user.is_authenticated and not request.method == 'POST':
        return render(request, 'login/index.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../todo')
        else:
            return render(request, 'login/index.html', {'error': 'User name and password do not match'})
    elif request.user.is_authenticated:
        return redirect('../todo')


def logout_view(request):
    logout(request)
    return redirect('../todo')


def dashboard(request):
    if request.user.is_authenticated:
        all_task = TodoList.objects.all().count()
        completed_task = TodoList.objects.filter(is_completed=1).count()
        upcoming_task = TodoList.objects.filter(is_completed=0).count()
        late_task = TodoList.objects.filter(is_completed=0, due_date__lt = date.today()).count()
        profiles = Profile.objects.get(user_id=request.user.id)
        return render(request, 'dashboard.html', {'profile': profiles, 'all_task': all_task, 'completed_task':
            completed_task, 'upcoming_task': upcoming_task, 'late_task': late_task})
    else:
        return redirect('../login')


def todo_view(request):
    todays_date = date.today()
    if request.user.is_authenticated and not request.method == 'POST':
        username = request.user.username
        todo_list = TodoList.objects.filter(username=request.user.id).order_by('due_date')
        profiles = Profile.objects.get(user_id=request.user.id)
        return render(request, 'todo.html', {'todo_list': todo_list, 'username': username, 'tdate': todays_date, 'profile': profiles})

    elif request.user.is_authenticated and request.method == 'POST':
        if 'up-id' in request.POST or 'completed-id' in request.POST:
            if 'completed-id' in request.POST:
                completed_id = request.POST['completed-id']
                completed_todo = TodoList.objects.get(id=int(completed_id))
                if completed_todo.is_completed:
                    completed_todo.is_completed = 0
                else:
                    completed_todo.is_completed = 1
                completed_todo.save()

            else:
                updated_id = request.POST['up-id']
                updated_todo = TodoList.objects.get(id=int(updated_id))
                updated_todo.todo = request.POST['todo']
                updated_todo.due_date = request.POST['due_date']
                updated_todo.save()
        else:
            deletedid = request.POST['del-id']
            deletedtodo = TodoList.objects.get(id=int(deletedid))
            deletedtodo.delete()
        todo_list = TodoList.objects.filter(username=request.user.id).order_by('due_date')
        profiles = Profile.objects.get(user_id=request.user.id)
        return render(request, 'todo.html', {'todo_list': todo_list, 'tdate': todays_date, 'profile': profiles})

    else:
        return redirect('../login')


def completed_todo_view(request):
    todays_date = date.today()
    if request.user.is_authenticated and not request.method == 'POST':
        username = request.user.username
        todo_list = TodoList.objects.filter(username=request.user.id, is_completed=1)
        profiles = Profile.objects.get(user_id=request.user.id)
        return render(request, 'completed-task.html', {'todo_list': todo_list, 'username': username,
                                                   'tdate': todays_date, 'profile': profiles})

    elif request.user.is_authenticated and request.method == 'POST':
        if 'up-id' in request.POST or 'completed-id' in request.POST:
            if 'completed-id' in request.POST:
                completed_id = request.POST['completed-id']
                completed_todo = TodoList.objects.get(id=int(completed_id))
                if completed_todo.is_completed:
                    completed_todo.is_completed = 0
                else:
                    completed_todo.is_completed = 1
                completed_todo.save()

            else:
                updated_id = request.POST['up-id']
                updated_todo = TodoList.objects.get(id=int(updated_id))
                updated_todo.todo = request.POST['todo']
                updated_todo.due_date = request.POST['due_date']
                updated_todo.save()
        else:
            deletedid = request.POST['del-id']
            deletedtodo = TodoList.objects.get(id=int(deletedid))
            deletedtodo.delete()
        todo_list = TodoList.objects.filter(username=request.user.id, is_completed=1)
        profiles = Profile.objects.get(user_id=request.user.id)
        return render(request, 'completed-task.html', {'todo_list': todo_list, 'tdate': todays_date, 'profile':
            profiles})

    else:
        return redirect('../login')


def upcoming_todo_view(request):
    todays_date = date.today()
    if request.user.is_authenticated and not request.method == 'POST':
        username = request.user.username
        todo_list = TodoList.objects.filter(username=request.user.id, is_completed=0)
        profiles = Profile.objects.get(user_id=request.user.id)
        return render(request, 'upcoming-todo.html', {'todo_list': todo_list, 'username': username,
                                                   'tdate': todays_date, 'profile': profiles})

    elif request.user.is_authenticated and request.method == 'POST':
        if 'up-id' in request.POST or 'completed-id' in request.POST:
            if 'completed-id' in request.POST:
                completed_id = request.POST['completed-id']
                completed_todo = TodoList.objects.get(id=int(completed_id))
                if completed_todo.is_completed:
                    completed_todo.is_completed = 0
                else:
                    completed_todo.is_completed = 1
                completed_todo.save()

            else:
                updated_id = request.POST['up-id']
                updated_todo = TodoList.objects.get(id=int(updated_id))
                updated_todo.todo = request.POST['todo']
                updated_todo.due_date = request.POST['due_date']
                updated_todo.save()
        else:
            deletedid = request.POST['del-id']
            deletedtodo = TodoList.objects.get(id=int(deletedid))
            deletedtodo.delete()
        todo_list = TodoList.objects.filter(username=request.user.id, is_completed=0)
        profiles = Profile.objects.get(user_id=request.user.id)
        return render(request, 'upcoming-todo.html', {'todo_list': todo_list, 'tdate': todays_date, 'profile':
            profiles})

    else:
        return redirect('../login')


def late_todo_view(request):
    todays_date = date.today()
    if request.user.is_authenticated and not request.method == 'POST':
        username = request.user.username
        todo_list = TodoList.objects.filter(username=request.user.id, is_completed=0, due_date__lt=date.today())
        profiles = Profile.objects.get(user_id=request.user.id)
        return render(request, 'late-todo.html', {'todo_list': todo_list, 'username': username,
                                                   'tdate': todays_date, 'profile': profiles})

    elif request.user.is_authenticated and request.method == 'POST':
        if 'up-id' in request.POST or 'completed-id' in request.POST:
            if 'completed-id' in request.POST:
                completed_id = request.POST['completed-id']
                completed_todo = TodoList.objects.get(id=int(completed_id))
                if completed_todo.is_completed:
                    completed_todo.is_completed = 0
                else:
                    completed_todo.is_completed = 1
                completed_todo.save()

            else:
                updated_id = request.POST['up-id']
                updated_todo = TodoList.objects.get(id=int(updated_id))
                updated_todo.todo = request.POST['todo']
                updated_todo.due_date = request.POST['due_date']
                updated_todo.save()
        else:
            deletedid = request.POST['del-id']
            deletedtodo = TodoList.objects.get(id=int(deletedid))
            deletedtodo.delete()
        todo_list = TodoList.objects.filter(username=request.user.id, is_completed=0, due_date__lt=date.today())
        profiles = Profile.objects.get(user_id=request.user.id)
        return render(request, 'late-todo.html', {'todo_list': todo_list, 'tdate': todays_date, 'profile':
            profiles})

    else:
        return redirect('../login')


def add_todo(request):
    added = 0
    if request.user.is_authenticated:
        if request.method == 'POST':
            todo = TodoList.objects.create(username=request.user, todo=request.POST['todo'], due_date=request.POST['due_date'])
            todo.save()
            added = 1
            profiles = Profile.objects.get(user_id=request.user.id)
            return render(request, 'addtodo.html', {'added': added, 'profile': profiles})
        else:
            profiles = Profile.objects.get(user_id=request.user.id)
            return render(request, 'addtodo.html',{'profile': profiles})
    else:
        return redirect('../login')


def settings_view(request):
    context = {}
    if request.method == "POST":
        form = ProfilesForm(request.POST, request.FILES)
        if form.is_valid():
            bio = form.cleaned_data.get("bio_field")
            img = form.cleaned_data.get("img_field")
            obj = Profile.objects.get(user_id= request.user.id)
            obj.profile_photo = img
            obj.bio = bio
            obj.save()
            context['profile'] = Profile.objects.get(user_id= request.user.id)
            return render(request, 'settings.html', context)
    else:
        profiles = Profile.objects.get(user_id= request.user.id)
        return render(request, 'settings.html', {'profile': profiles})