from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def create_user(request):
    name_form = request.POST['name']
    email_form = request.POST['email']
    language_form = request.POST['language']
    location_form = request.POST['location']

    context = {
        "name_template" : name_form,
        "email_template" : email_form,
        "language_template" : language_form,
        "location_template" : location_form,
    }
    return render(request, 'result.html', context)
