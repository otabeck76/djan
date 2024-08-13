from django.shortcuts import render # type: ignore

def index(request):
    return render(request, 'index.html')

def my_view (request):
    menu_items=[
        {'name':"Home","url":"index",'active': True},
         {'name':"Home","url":"index",'active': True},
          {'name':"Home","url":"index",'active': True},
            {'name':"Home","url":"index",'active': True},
    ]
    return render(request,'index.html',{'menu_items':menu_items})
