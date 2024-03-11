from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import TodoForm
from django.views.generic import ListView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

# Create your views here.

#list view codes
class TaskListView(ListView):
    model=Task
    template_name='home.html'
    context_object_name = 'task' #the object used to fetch the objects from Task.


class TaskDetailView(DetailView):
    model=Task
    template_name='details.html'
    context_object_name = 'task' #the object used to fetch the objects from Task.


class TaskUpdateView(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name = 'task' #the object used to fetch the objects from Task.
    fields=['name','priority','date']

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id}) #cbvdetail is the "name=?" value for cbvdetail path in urls page

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')





#previous view codes
def add(request):
    task1 = Task.objects.all()
    if request.method=='POST': #get the name and priority from screen
        name=request.POST.get('name') #name given in home.html file
        priority=request.POST.get('priority')
        date = request.POST.get('date')
        task=Task(name=name,priority=priority,date=date)
        task.save()  # add to db:
    return render(request,"home.html",{'task':task1})

# def details(request):
#     task = Task.objects.all()
#     return render(request,"details.html",{'task':task})

def delete(request, taskid):
    if request.method =='POST':
        task = Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(request,"delete.html")


def update(request, taskid):
    task = Task.objects.get(id=taskid)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"edit.html",{'f':f,'task':task})