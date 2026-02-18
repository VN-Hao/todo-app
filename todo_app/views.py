from django.shortcuts import render, redirect
from .models import TaskModel

# Create your views here.


def main_app(request):
    all_tasks = TaskModel.objects.all()

    return render(request, "todo_app/index.html", {
        "all_tasks": all_tasks
    })


def add_task(request):
    TaskModel.objects.create(
        task_description=request.POST["task"],
        is_done=False
    )

    return redirect("app-page")

def remove_task(request):
    task = request.POST["task"]
    TaskModel.objects.get(task_description=task).delete()
    return redirect("app-page")

def update_status(request):
    pass
