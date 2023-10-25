

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.

def index(request):
    title = "My first project"
    return render(request, 'index.html', {

        'title': title,
        'name': 'Javi'

        })
    #return HttpResponse("<h2>index </h2>" )

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("<h2>About page</h2>")

def hello(request, username):
    return HttpResponse("<h2>Hello %s </h2>" % username )

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects': projects
    })

    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request):
    task = Task.objects.all()
    return render(request, 'tasks/task.html',{"tasks": task})

    #task = get_object_or_404(Task, title=title)
    task = Task.objects.get(title=title)
    return HttpResponse("<h2>tasks: %s </h2> " % task.title)
    task = Task(title="New Task", description="New Description")
    task.save()
    return HttpResponse("<h2>Task created</h2>")

def createTask(request):
    if(request.method == 'GET'):
        return render(request, 'tasks/create_task.html',{ "form": CreateNewTask() })
    else:
        Task.objects.create(
            title=request.POST.get('title'), 
            description=request.POST.get('description'), 
            project_id=3
        )
        render(request, 'tasks/create_task.html',{ "form": CreateNewTask() })
        return redirect('tasks')

def createProject(request):
    if(request.method == 'GET'):
        return render(request, 'projects/create_projects.html',{'form': CreateNewProject()})
    else:
        Project.objects.create(
            name= request.POST.get('name'),
            description = request.POST.get('description')
        )
        render(request, 'projects/create_projects.html',{'form':CreateNewProject()})
        return redirect('projects')


    