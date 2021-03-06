from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class Reminder(models.Model):
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('published', 'Published'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)







    def __str__(self):
        return self.name
