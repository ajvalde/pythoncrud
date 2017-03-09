from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class Remember(models.Model):
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('published', 'Published'),
    )
    reminder_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('reminderit:post_detail', kwargs={'reminder_id': self.reminder_id})




    def __str__(self):
        return self.name
