from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.core import serializers
from .models import *
import json

# Create your views here.

def mylogin(request):
    if (request.user.is_authenticated()):
        return redirect('home')
    if(request.method == 'GET'):
        form = AuthenticationForm()
        return render(request, 'account/login.html', {'form': form})
    else:
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        return render(request, 'account/login.html', {'form' : form})

@login_required
def home(request):
    return render(request, 'account/home.html')

@login_required
def mylogout(request):
    logout(request)
    return redirect('login')

@login_required
@require_http_methods(["GET"])
def autocomplete(request):
    term = request.GET.get('term', '')
    print (term)
    if (term == ''):
        data = []
    else:
        users = MyUser.objects.filter(username__icontains = term)
        data = [ {'label': user.get_full_name(), 'value' : user.id } for user in users ]
    return HttpResponse(json.dumps(data), content_type = 'application/json')        


    
    



