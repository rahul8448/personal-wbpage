from django.db import models
from django.utils.encoding import smart_unicode


# Creating your message form model.

class Message(models.Model):
    full_name=models.CharField(max_length=50,null=False,blank=False)
    phone_num=models.CharField(max_length=15,null=True,blank=True)
    email=models.EmailField(null=False,blank=False)
    company=models.CharField(max_length=50,null=True,blank=True)
    subject=models.CharField(max_length=40,blank=False,null=True)
    message=models.CharField(max_length=200,null=True,blank=True)
    create_time=models.DateTimeField(auto_now_add=True,auto_now=False)
    update_time=models.DateTimeField(auto_now_add=False,auto_now=True)


def __unicode__(self):
    return smart_unicode(self.email)