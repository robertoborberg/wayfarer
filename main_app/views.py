from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import ProfileForm, PostForm
from .models import Profile, Post, City

# Create your views here.
def home(request):
    return render(request, 'home.html')

def city_index(request):
    cities = City.objects.all()
    return render(request, 'city/index.html', {'cities': cities})

def city_detail(request, city_id):
    city = City.objects.get(id = city_id)
    posts = Post.objects.filter(city_id = city.id)
    context = {
        'city': city,
        'posts': posts,
    }
    return render(request, 'city/detail.html', context)

def city_post(request):
    return render(request, 'city/post.html')

def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = request.user
            login(request, user)
            return redirect(f'/profile/{user.id}', {'user': user})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

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

def update(request, user_id):
    profile = Profile.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect(f'/profile/{profile.user_id}', {'profile': profile})
        else:
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'registration/update.html', {'form': form, 'profile': profile, 'user_id': user_id})

def profile(request, user_id):
    profile = Profile.objects.get(user_id = user_id)
    posts = Post.objects.filter(profile_id = profile.id)
    print(profile.name)
    return render(request, 'profile.html', {'user_id':user_id, 'profile':profile, 'posts': posts})

def post_new(request, city_id):
    city = City.objects.get(id=city_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.city_id = city_id
            post.save()
            return redirect('city_index')
        else:
            return redirect('/post/new')
    else:
        form = PostForm()
        return render(request, 'post_new.html', {'form': form, 'city': city, 'profile': profile})        

def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post_id)
        else:
            print(form)
            return redirect('post_edit', post_id)
    else:
        form = PostForm()
        return render(request, 'post_edit.html', {'form': form})

def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    profile = Profile.objects.get(id = post.profile_id)
    city = City.objects.get(id = post.city_id)
    context = {
        'post': post,
        'profile': profile,
        'city': city,
    }
    return render(request, 'post.html', context)

def post_delete(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('home')