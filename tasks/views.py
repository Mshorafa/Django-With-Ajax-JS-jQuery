from django.shortcuts import render,redirect
from django.views import generic
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .forms import TaskForm
from .models import DoTask

# Create your views here.


class TaskList(generic.View):
    def get(self,request):
        form = TaskForm()
        tasks = DoTask.objects.all()
        context = {
            'form':form,
            'tasks':tasks
        }
        return render(request,'tasks/TaskList.html',context)

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            print(form)
            newTask=form.save()
            return JsonResponse({'task':model_to_dict(newTask)},status=200)
        else:
            return redirect('task:TaskListUrl')


class CompletedTask(generic.View):
    def post(self,request, id):
        task = DoTask.objects.get(id=id)
        task.completaed = True
        task.save()

        return JsonResponse({'task':model_to_dict(task)},status=200)


class removeTask(generic.View):
    def post(self, request, id):
        task = DoTask.objects.get(id=id)
        task.delete()
        return JsonResponse({'task': model_to_dict(task)}, status=200)