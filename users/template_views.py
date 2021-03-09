
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect ,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login 
from django.http import HttpResponseNotFound
from django.contrib.auth import views as auth_views
# from django.contrib.auth.models import User
from .models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import  SignUpForm ,LoginForm


@login_required(login_url='/user/login')
def user_page(request):
 
    # return redirect(reverse('users:user_page'))
    return render(request, 'users/page-user.html',{'user': request.user})

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "registration/login.html", {"form": form, "msg" : msg})


def register(request):
    """Responsible for validation and creation of new users.

    Check if all required inputs are filled, if password and
    password confirmation are equal, if user with posted username
    already not exists and then create new user with possible friend username
    or blank string. After succesed registration proceed authentication
    and redirect to index path, otherwise return error messages to source
    registration form.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')  
            user = authenticate(username=username, password=raw_password)  

            user.save()
            
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})