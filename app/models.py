# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Moment(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=20)
    kind = models.CharField(max_length=20)

# Create your models here.
