from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record

# Home page
def home(request):
  return render(request, 'webapp/index.html')

# Register a user
def register(request):
  form = CreateUserForm(request.POST)
  if request.method == "POST":
    if form.is_valid():
      form.save()
      return redirect('my_login')
      
  context = {'form' : form}
  return render(request, 'webapp/register.html', context=context)


# login a user
def my_login(request):
  
  form = LoginForm()
  if request.method == "POST":
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
      username = request.POST.get('username')
      password = request.POST.get('password')
      
      user = authenticate(request, username=username, password=password)
      
      if user is not None:
        auth.login(request, user)
        
        return redirect('dashboard')
        
  context = {'login_form' : form}
  return render(request, 'webapp/my-login.html', context=context)

# - Dashboard
@login_required(login_url='my_login')
def dashboard(request):
  my_records = Record.objects.all()
  context = {'records' : my_records}
  return render(request, 'webapp/dashboard.html')

# user log out 
def user_logout(request):
  auth.logout(request)
  
  return redirect("my_login")

