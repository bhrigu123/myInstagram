from django.db import models
from django.conf import settings
import uuid,datetime
from django.utils import timezone

# Create your models here.
DEFAULT_EXPIRATION_PERIOD_IN_DAYS = 45
def get_token_for_user(user):
    token = AuthToken.objects.filter(user = user)
    if (len(token) > 0) :
        token = token[0]
    else:
        token = None
    if token is not None and token.is_expired():
        token.status = 'E'
        token.save()
        token = None
    if token is None:
        string = uuid.uuid1().hex
        while (len(AuthToken.objects.filter(token = string)) > 0):
            string = uuid.uuid1().hex
        expires_on = datetime.datetime.now() + datetime.timedelta(days = DEFAULT_EXPIRATION_PERIOD_IN_DAYS)
        token = AuthToken.objects.create(user = user, token = string, expires_on = expires_on)
        return token;
    else:
        return token
class AuthToken(models.Model):
    STATUS = (('E', 'Expired'), ('V', 'Valid'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    token = models.CharField(max_length = 100, unique = True)
    status = models.CharField(max_length = 1, choices= STATUS, default = 'V')
    created_on = models.DateTimeField(auto_now_add = True)
    expires_on = models.DateTimeField()

    def is_expired(self):
        return self.status == 'Expired' or self.expires_on < timezone.now()
