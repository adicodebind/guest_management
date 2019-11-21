from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from registration.forms import RegisterForm
from registration.models import User, Host


def signup(request):
    if request.method == "POST":
        new_user_form = RegisterForm(request.POST)
        if new_user_form.is_valid():
            
            current_user = User.objects.filter(email=new_user_form.cleaned_data['email']).first()

            if not current_user:
                new_user = User.objects.create_user(
                    username=new_user_form.cleaned_data["email"],
                    password=new_user_form.cleaned_data["password"],
                    email=new_user_form.cleaned_data["email"]
                )

                new_user.first_name = new_user_form.cleaned_data["first_name"]
                new_user.last_name = new_user_form.cleaned_data["last_name"]
                new_user.save()
                current_user = new_user

            host = Host.objects.create(user=current_user)
            login(request, current_user)
            return redirect('/')
        else:
            return render(request, 'registration/register.html', {"form": new_user_form})
    else:
        new_form = RegisterForm()
        return render(request, 'registration/register.html', {"form": new_form})
