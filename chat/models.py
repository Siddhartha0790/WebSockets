from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Messages(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', default = None, on_delete=models.PROTECT)
    to_user = models.ForeignKey(User, related_name='to_user', default = None, on_delete=models.PROTECT)
    data = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now=True)
    seen = models.BooleanField(default=False)
    
class userChannel(models.Model):
    user = models.ForeignKey(User , on_delete=models.PROTECT , default=None)
    channel_name = models.CharField(max_length=1000 , blank = False , null = False )