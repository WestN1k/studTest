from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.
# @login_required()
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username, password)
    # if user is not None:
    #     if user.is_active:
    #         login(request, user)
    #         # Redirect to a success page.
    #     else:
    #         # Return a 'disabled account' error message
    #         ...
    # else:
    #     # Return an 'invalid login' error message.
    #     ...
    return render(request, 'login/login.html', context={'hello': 'привет пользователь'})


def user_logout(request):
    return render(request, 'login/login.html', context={'hello': 'привет пользователь'})