# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    def __unicode__(self):
        return self.first_name+" "+self.last_name    
   
