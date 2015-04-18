from django.shortcuts import render
import json
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import *


# Create your views here.
@csrf_exempt
@require_http_methods(['POST'])
def apilogin(request):
    u = request.POST.get('username')
    p = request.POST.get('password')
    user = authenticate(username = u, password = p)
    if user is None:
        return HttpResponse(json.dumps({'error':'Invalid Username or Password'}), status = 400, content_type = 'application/json')
    if not user.is_active:
        return HttpResponse(json.dumps({'error':'Inactive User'}), status = 403, content_type = 'application/json')
    token = get_token_for_user(user)
    return HttpResponse(json.dumps({'id' : user.id, 'token': token.token}), status = 200, content_type = 'application/json')








