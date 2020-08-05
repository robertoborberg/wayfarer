from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def city_index(request):
    return render(request, 'city/index.html')

def signup(request):
    error_message = 'Error'
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message,
    }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            global error 
            error = 'User account already exists'
            return render(request, 'registration/signup.html', context)
    else:
        return render(request, 'registration/signup.html', context)