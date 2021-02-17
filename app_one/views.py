from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def create_user(request):
    name_form = request.POST['name']
    email_form = request.POST['email']
    context = {
        "name_template" : name_form,
        "email_template" : email_form,
    }
    return render(request, 'result.html', context)

