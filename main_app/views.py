from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile
# Create your views here.
def home(request):
    return render(request, 'home.html')

def city_index(request):
    return render(request, 'city/index.html')

def city_detail(request):
    return render(request, 'city/detail.html')

def city_post(request):
    return render(request, 'city/post.html')

def signup(request):
    error_message = 'Error'
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message,
    }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form2 = ProfileForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile = form2.save(commit=False)
            profile.user_id = user.id
            profile.save()
            
            
            return redirect(f'/profile/{user.id}', { 'user': user, 'profile': profile } )
        else:
            global error 
            error = 'User account already exists'
            return render(request, 'registration/signup.html', context)
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

def update(request):
    form = ProfileForm()
    # print(user)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save()
            return render('profile.html', {'profile': profile})
        else:
            return redirect('home')
    else:
        form = ProfileForm()
        return render('registration/update.html', {'form': form})

def profile(request, user_id):
    profile = Profile.objects.get(user_id = user_id)
    return render(request, 'profile.html', {'user_id':user_id, 'profile':profile})