from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import LogInForm

class MainView():
    def main_page(request):
        return render(request, 'main.html')

    @login_required
    def about(request):
        return render(request, 'about.html')

class AuthenticateView():
    def login_view(request):
        form = LogInForm()
        if request.method == 'POST':
            if form.is_valid():
                _username = form.cleaned_data['username']
                _password = form.cleaned_data['password']
                user = authenticate(username=_username, password=_password)
                if user is not None:
                    if user.is_active:
                        return redirect('')
                    else:
                        return redirect('login.html')
        context = {
            'form': form
        }
        return render(request, 'login.html', context)

    def logout_view(request):
        if request.user.is_authenticated():
            logout(request)
        return redirect('/')
