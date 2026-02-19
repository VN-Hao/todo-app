from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import TaskModel
import json

# Create your views here.


def main_app(request):
    all_tasks = TaskModel.objects.all()

    return render(request, "todo_app/index.html", {
        "all_tasks": all_tasks
    })


def add_task(request):
    print(request.POST)
    TaskModel.objects.create(
        task_description=request.POST["task"],
        is_done=False
    )

    return redirect("app-page")

def remove_task(request):
    print(request.POST)
    task = request.POST["task"]
    TaskModel.objects.get(task_description=task).delete()
    return redirect("app-page")

def update_status(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        task_desc = data.get("task_description")
        is_done = data.get("isDone")
        
        try:
            task = TaskModel.objects.get(task_description=task_desc)
            task.is_done = is_done
            task.save()
            return JsonResponse({"message": "Task updated successfully", "is_done": task.is_done})
        except TaskModel.DoesNotExist:
            return JsonResponse({"error": "Task not found"}, status=404)
            
    return JsonResponse({"error": "Invalid request method"}, status=400)
