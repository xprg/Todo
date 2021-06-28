from django import http
from django.http.response import HttpResponseRedirect
from main.models import TodoList
from django.shortcuts import render
from .forms import CreateList
from django.http import HttpResponse



def empty(response):
    return HttpResponse("<h1>hello there</h1>")

def index(response):
    return render(response,'main/view.html',{})

def home(response):
    return render(response,"main/home.html",{})

def show(response,id):
    td=TodoList.objects.get(id=id)
    
    if response.method=="POST":
        if response.POST.get('save'):
            
            for item in td.item_set.all():
                if response.POST.get("c"+ str(item.id)) == "clicked" :

                    item.done=True
                    
                else:
                    item.done=False

                item.save()

        elif response.POST.get('new_item'):
            txt=response.POST.get('new_item_text')
            
            if len(txt)>2:
                td.item_set.create(text=txt,done=False)
                td.save()
            else:
                print('name too small')


    

    for i in td.item_set.all():
        print(i.done)
   
    
    return render(response,'main/list.html',{'list':td})

def create(response):

    if response.method=='POST':
        
        
        form=CreateList(response.POST)

        if form.is_valid():
            todo_name=form.cleaned_data['name']
            response.user.todolist_set.create(todo_name)
            
            return HttpResponseRedirect('/view')
        
        

        

    else:
        form=CreateList()
        return render(response,'main/create.html',{'form':form})

        
    
