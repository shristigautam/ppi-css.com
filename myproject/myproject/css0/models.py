# -*- coding: utf-8 -*-
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')


class Scores(models.Model):
	name = models.CharField(max_length=30)
	score = models.FloatField()
	interface = models.CharField(max_length=30)
	uploaded = models.BooleanField(default=False) 
	date_uploaded = models.DateTimeField(auto_now_add=False)

