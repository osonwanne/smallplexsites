from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):

    Name = models.CharField("Name", max_length=100, null=True, blank=True)
    Email = models.EmailField("Email")
    Message = models.TextField("Message", blank=True)
    Created = models.DateTimeField("Created", auto_now=True)