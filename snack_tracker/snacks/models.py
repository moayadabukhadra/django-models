from ssl import Options
from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    name = models.CharField(max_length=64, null=True,blank=True)
    purchaser = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    description = models.TextField()

