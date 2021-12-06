from django.db import models

class Hospital(models.Model):
    nome = models.CharField(max_length=50)