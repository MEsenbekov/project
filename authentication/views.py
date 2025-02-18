from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})


def books_list(request):
    return render(request, 'Books/books_list.html')


class UserLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

# Create your views here.
