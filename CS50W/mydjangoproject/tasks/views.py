from django import forms
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label= "New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

tasks = [] 
def index(request):
    # if "tasks" not in request.session:
    #     request.session["tasks"] = [] 
        
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
    
def addtask(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST) # get all the data the user submited wwithin POST and store in in form variable
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form" : form
            })
        
    return render(request,"tasks/add.html", {
        "form": NewTaskForm()
    })
