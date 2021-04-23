from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

def todo(request):
    todos=Todo.objects.all()

    form=TodoForm()
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'todos':todos,'form':form}
    return render(request,'index.html',context)
def updateTask(request, pk):
    task=Todo.objects.get(id=pk)
    form=TodoForm(instance=task)
    if request.method == 'POST':
           form=TodoForm(request.POST, instance=task)
           if form.is_valid():
               form.save()
               return redirect('/') 

    context={'form':form}
    return render(request,'update.html',context)

  
  
def deleteitem(request,pk):
    try:

        item=Todo.objects.get(id=pk)
        messages.success(request, f"{item} has been deleted")

        item.delete()
    except Todo.DoesNotExist:
        messages.info(request, "Following item doesn't exist")    
    return redirect('/') 