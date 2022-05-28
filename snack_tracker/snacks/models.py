from ssl import Options
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
    name = models.CharField(max_length=64, null=True,blank=True)
    purchaser = models.ForeignKey(get_user_model(), on_delete= models.CASCADE, null=True, blank=True)
    description = models.TextField()
    
    def get_absolute_url(self):
        return reverse('snack_detail', kwargs={'pk': self.pk})


