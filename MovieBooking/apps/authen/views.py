from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from . forms import NewUserForm, Profile
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username},Your account has created successfully')
            form.save()
            return redirect('/')

    else:
        form = NewUserForm()
    my_forms = {'form': form}
    return render(request, "authen/signup.html", my_forms)


def login_request(request):
    print("hello")
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "authen/login.html",
                    context={"form":form})
@login_required
def profilepage(request):
    form = NewUserForm(request.POST, request.FILES)
    profile_form = Profile(request.POST, request.FILES)
    if form.is_valid() and profile_form.is_valid():
        username = form.cleaned_data.get('username')
        print(username)
        user = form.save()
        profile_new = profile_form.save(commit=False)
        profile_new.user = user
        return redirect('index')
    return render(request, 'authen/profile.html')


def logout_request(request):
  if request.method == 'POST':
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')
