from .models import *
from django.http import HttpResponse
import json
class CustomTokenAuthMiddleware(object):
    def process_request(self, request):
        print(request.user)
        if (request.user is not None and request.user.is_anonymous() == False):
            return
        token = request.META.get('HTTP_AUTHORIZATION')
        if (token != ''):
            try:
                token = AuthToken.objects.get(token = token)
            except AuthToken.DoesNotExist:
                return
            if (token.is_expired()):
                return HttpResponse(json.dumps({'error':'Expired Access Token'}), status = 403, content_type = 'application/json')
            request.user = token.user
            return


            





