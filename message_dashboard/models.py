from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class DashBoard_Messages(models.Model):
    sender_name=models.CharField(max_length=20,null=False,blank=False)
    sender_organization=models.CharField(max_length=30,null=False,blank=False)
    sender_email=models.CharField(max_length=20,null=False,blank=False)
    sender_phone=models.CharField(max_length=30,null=True,blank=True)
    message_subject=models.CharField(max_length=50,null=False,blank=False)
    message_body=models.CharField(max_length=200,null=True,blank=True)
    is_read=models.BooleanField(default=False)
    create_time=models.DateTimeField(auto_now_add=True,auto_now=False)

    class Meta:
       db_table = 'dashboard_messages'


def __unicode__(self):
    return smart_unicode(self.email)