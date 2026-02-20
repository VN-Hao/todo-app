from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import TaskModel, UserModel
import json
import hashlib

# Create your views here.


def login(request, status_msg="", status_code=200):
    return render(
        request, "todo_app/login.html", {"status": status_msg}, status=status_code
    )


def verify_credential(request):
    username = request.POST["username"]
    password = request.POST["password"]

    try:
        user = UserModel.objects.get(username=username)
        hashed_password = hashlib.sha256(password.encode("UTF-8")).hexdigest()

        if user.hashed_password != hashed_password:
            return login(request, status_msg="Incorrect password", status_code=401)

        return redirect("app-page")
    except UserModel.DoesNotExist:
        return login(request, status_msg="Invalid username", status_code=401)


def main_app(request):
    all_tasks = TaskModel.objects.all()

    return render(request, "todo_app/index.html", {"all_tasks": all_tasks})


def add_task(request):
    TaskModel.objects.create(task_description=request.POST["task"], is_done=False)

    return redirect("app-page")


def remove_task(request):
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
            return JsonResponse(
                {"message": "Task updated successfully", "is_done": task.is_done}
            )
        except TaskModel.DoesNotExist:
            return JsonResponse({"error": "Task not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=400)
