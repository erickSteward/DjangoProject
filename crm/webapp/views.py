from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

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
        
        # return redirect('')
        
  context = {'login_form' : form}
  return render(request, 'webapp/my-login.html', context=context)

# user log out 
    